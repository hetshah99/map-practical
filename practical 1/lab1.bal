import ballerina/io;
import ballerina/lang.'int as langint;

function add(int|error a,int|error b) returns(int|error)
{
	return a+b;
}

public function main()
{
	string choice1 = io:readln("Enter num1");
	string choice2 = io:readln("Enter num2 ");

	int|error a = langint:fromString(choice1);
	int|error b = langint:fromString(choice2);
	
	io:println(add(a,b));
		
}

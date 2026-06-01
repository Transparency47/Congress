# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3869?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3869
- Title: Healthy Families Act
- Congress: 119
- Bill type: S
- Bill number: 3869
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-05-15T11:03:25Z
- Update date including text: 2026-05-15T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3869",
    "number": "3869",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "Healthy Families Act",
    "type": "S",
    "updateDate": "2026-05-15T11:03:25Z",
    "updateDateIncludingText": "2026-05-15T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-02-12T19:30:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "WA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "WI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "DE"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "AZ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "VA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-02-12",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "RI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "HI"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "OR"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "OR"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "RI"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3869is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3869\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Sanders (for himself, Mr. Schumer , Mrs. Murray , Ms. Baldwin , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Ms. Cantwell , Mr. Coons , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Gallego , Mrs. Gillibrand , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. King , Ms. Klobuchar , Mr. Markey , Mr. Murphy , Mr. Padilla , Mr. Reed , Mr. Schatz , Ms. Slotkin , Ms. Smith , Mr. Van Hollen , Mr. Welch , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo allow Americans to earn paid sick time so that they can address their own health needs and the health needs of their families.\n#### 1. Short title\nThis Act may be cited as the Healthy Families Act .\n#### 2. Definitions\nIn this Act:\n**(1) Child**\nThe term child means, regardless of age, a biological, foster, or adopted child, a stepchild, a child of a domestic partner, a legal ward, or a child of a person standing in loco parentis.\n**(2) Commerce**\nThe terms commerce and industry or activity affecting commerce mean any activity, business, or industry in commerce or in which a labor dispute would hinder or obstruct commerce or the free flow of commerce, and include commerce and any industry affecting commerce , as defined in paragraphs (1) and (3) of section 501 of the Labor Management Relations Act, 1947 (29 U.S.C. 142 (1) and (3)).\n**(3) Domestic partner**\n**(A) In general**\nThe term domestic partner , with respect to an individual, means another individual with whom the individual is in a committed relationship.\n**(B) Committed relationship defined**\nThe term committed relationship means a relationship between 2 individuals, each at least 18 years of age, in which each individual is the other individual\u2019s sole domestic partner and both individuals share responsibility for a significant measure of each other\u2019s common welfare. The term includes any such relationship between 2 individuals, including individuals of the same sex, that is granted legal recognition by a State or political subdivision of a State as a marriage or analogous relationship, including a civil union or domestic partnership.\n**(4) Domestic violence**\nThe term domestic violence has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ), except that the reference in such section to the term jurisdiction receiving grant funding shall be deemed to mean the jurisdiction in which the victim lives or the jurisdiction in which the employer involved is located.\n**(5) Employee**\nThe term employee means an individual who is\u2014\n**(A)**\n**(i)**\nan employee, as defined in section 3(e) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(e) ), who is not covered under any other provision of this paragraph, including such an employee of the Library of Congress, except that a reference in such section to an employer shall be considered to be a reference to an employer described in paragraph (6)(A)(i)(I);\n**(ii)**\nan employee of the Government Accountability Office; or\n**(iii)**\nan employee of a covered employer described in paragraph (6)(B)(i)(IV) who performs work that has been traditionally performed by employees in a railroad industry craft or class recognized under the Ninth paragraph of section 2 of the Railway Labor Act ( 45 U.S.C. 152 ), including any employee who performs\u2014\n**(I)**\nwork with respect to the movement of trains;\n**(II)**\nmaintenance of way work;\n**(III)**\nsignal work;\n**(IV)**\nwork for purposes of the inspection, maintenance, repair, or cleaning of locomotives, rail maintenance facilities, rail-related equipment, or rail cars;\n**(V)**\ndispatching work;\n**(VI)**\nwork with respect to the movement of equipment within a rail yard; or\n**(VII)**\nrail clerical or communications work;\n**(B)**\na State employee described in section 304(a) of the Government Employee Rights Act of 1991 (42 U.S.C. 2000e\u201316c(a));\n**(C)**\na covered employee, as defined in section 101 of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 ), other than an applicant for employment;\n**(D)**\na covered employee, as defined in section 411(c) of title 3, United States Code; or\n**(E)**\na Federal officer or employee covered under subchapter V of chapter 63 of title 5, United States Code (without regard to the limitation in section 6381(1)(B) of that title).\n**(6) Employer**\n**(A) In general**\nThe term employer means a person who is\u2014\n**(i)**\n**(I)**\na covered employer who is not described in any other subclause of this clause;\n**(II)**\nan entity employing a State employee described in section 304(a) of the Government Employee Rights Act of 1991;\n**(III)**\nan employing office, as defined in section 101 of the Congressional Accountability Act of 1995;\n**(IV)**\nan employing office, as defined in section 411(c) of title 3, United States Code; or\n**(V)**\nan employing agency covered under subchapter V of chapter 63 of title 5, United States Code; and\n**(ii)**\nengaged in commerce (including government), or an industry or activity affecting commerce (including government).\n**(B) Covered employer**\n**(i) In general**\nIn subparagraph (A)(i)(I), the term covered employer \u2014\n**(I)**\nmeans any person engaged in commerce or in any industry or activity affecting commerce who employs 1 or more employees for each working day during each of 20 or more calendar workweeks in the current or preceding year;\n**(II)**\nmeans the Government Accountability Office and the Library of Congress;\n**(III)**\nincludes\u2014\n**(aa)**\nany person who acts, directly or indirectly, in the interest of an employer covered by this clause to any of the employees of such employer; and\n**(bb)**\nany successor in interest of such an employer; and\n**(IV)**\nincludes any rail carrier.\n**(ii) Public agency**\nFor purposes of clause (i), a public agency, as defined in section 3(x) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(x) ), shall be considered to be a person engaged in commerce or in an industry or activity affecting commerce.\n**(iii) Definitions**\nFor purposes of this subparagraph:\n**(I) Employee**\nThe term employee has the meaning given such term in section 3(e) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(e) ).\n**(II) Person**\nThe term person has the meaning given such term in section 3(a) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(a) ).\n**(C) Predecessors**\nAny reference in this paragraph to an employer shall include a reference to any predecessor of such employer.\n**(7) Employment benefits**\nThe term employment benefits means all benefits provided or made available to employees by an employer, including group life insurance, health insurance, disability insurance, sick leave, annual leave, educational benefits, and pensions, regardless of whether such benefits are provided by a practice or written policy of an employer or through an employee benefit plan , as defined in section 3(3) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(3) ).\n**(8) Health care provider**\nThe term health care provider means a provider who\u2014\n**(A)**\n**(i)**\nis a doctor of medicine or osteopathy who is authorized to practice medicine or surgery (as appropriate) by the State in which the doctor practices; or\n**(ii)**\nis any other person determined by the Secretary to be capable of providing health care services; and\n**(B)**\nis not employed by an employer for whom the provider issues certification under this Act.\n**(9) Paid sick time**\nThe term paid sick time means an increment of compensated leave that\u2014\n**(A)**\ncan be earned by an employee for use during an absence from employment for any of the reasons described in paragraphs (1) through (4) of section 3(b); and\n**(B)**\nis compensated at a rate that is not less than the greater of\u2014\n**(i)**\nthe regular rate of pay of the employee;\n**(ii)**\nthe rate specified in section 6(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(a)(1) ); or\n**(iii)**\nthe rate specified in the applicable State or local minimum wage law.\n**(10) Parent**\nThe term parent means a biological, foster, or adoptive parent of an employee, a stepparent of an employee, parent-in-law, parent of a domestic partner, or a legal guardian or other person who stood in loco parentis to an employee when the employee was a child.\n**(11) Rail carrier**\nThe term rail carrier has the meaning given such term in section 10102 of title 49, United States Code.\n**(12) Secretary**\nThe term Secretary means the Secretary of Labor.\n**(13) Sexual assault**\nThe term sexual assault has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(14) Spouse**\nThe term spouse , with respect to an employee, has the meaning given such term by the marriage laws of the State in which the marriage was celebrated.\n**(15) Stalking**\nThe term stalking has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(16) State**\nThe term State has the meaning given the term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(17) Victim services organization**\nThe term victim services organization means a nonprofit, nongovernmental organization that provides assistance to victims of domestic violence, sexual assault, or stalking or advocates for such victims, including a rape crisis center, an organization carrying out a domestic violence, sexual assault, or stalking prevention or treatment program, an organization operating a shelter or providing counseling services, or a legal services organization or other organization providing assistance through the legal process.\n#### 3. Earned paid sick time\n##### (a) Earning of paid sick time\n**(1) In general**\nAn employer shall provide each employee employed by the employer not less than 1 hour of earned paid sick time for every 30 hours worked, to be used as described in this section. An employer shall not be required to permit an employee to earn, under this section, more than 56 hours of paid sick time in a year, unless the employer chooses to set a higher limit.\n**(2) Exempt employees**\n**(A) In general**\nExcept as provided in subparagraph (B), for purposes of this section, an employee who is exempt from overtime requirements under section 13(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 213(a)(1) ) shall be deemed to work 40 hours in each workweek.\n**(B) Shorter normal workweek**\nIf the normal workweek of such an employee is less than 40 hours, the employee shall earn paid sick time based upon that normal workweek.\n**(3) Dates for beginning to earn paid sick time and use**\nExcept as provided in the second sentence of paragraph (7), employees shall begin to earn paid sick time under this section at the commencement of their employment. Except as provided in such sentence, an employee shall be entitled to use the earned paid sick time beginning on the 60th calendar day following commencement of the employee's employment. After that 60th calendar day, the employee may use the paid sick time as the time is earned. An employer may, at the discretion of the employer, loan paid sick time to an employee for use by such employee in advance of the employee earning such sick time as provided in this subsection and may permit use before the 60th day of employment.\n**(4) Carryover**\n**(A) In general**\nExcept as provided in subparagraph (B), paid sick time earned under this section shall carry over from 1 year to the next.\n**(B) Construction**\nThis Act shall not be construed to require an employer to permit an employee to earn more than 56 hours of earned paid sick time in a calendar year.\n**(5) Employers with existing policies**\nAny employer with a paid leave policy who makes available an amount of paid leave that is sufficient to meet the requirements of this section and that may be used for the same purposes and under the same conditions and procedures as the purposes, conditions, and procedures described in this section shall not be required to permit an employee to earn additional paid sick time under this section.\n**(6) Construction**\nNothing in this section shall be construed as requiring financial or other reimbursement to an employee from an employer upon the employee\u2019s termination, resignation, retirement, or other separation from employment for earned paid sick time that has not been used.\n**(7) Reinstatement**\nIf an employee is separated from employment with an employer and is rehired, within 12 months after that separation, by the same employer, the employer shall reinstate the employee\u2019s previously earned paid sick time. The employee shall be entitled to use the earned paid sick time and earn additional paid sick time at the recommencement of employment with the employer.\n**(8) Prohibition**\nAn employer may not require, as a condition of providing paid sick time under this Act, that the employee involved search for or find a replacement employee to cover the hours during which the employee is using paid sick time.\n##### (b) Uses\nPaid sick time earned under subsection (a) may be used by an employee for any of the following:\n**(1)**\nAn absence resulting from a physical or mental illness, injury, or medical condition of the employee.\n**(2)**\nAn absence resulting from obtaining professional medical diagnosis or care, or preventive medical care, for the employee.\n**(3)**\nAn absence for the purpose of caring for a child, a parent, a spouse, a domestic partner, or any other individual related by blood or affinity whose close association with the employee is the equivalent of a family relationship, who\u2014\n**(A)**\nhas any of the conditions or needs for diagnosis or care described in paragraph (1) or (2);\n**(B)**\nis required to attend\u2014\n**(i)**\nin the case of someone who is a child, a school meeting; or\n**(ii)**\na meeting at a place where the child, parent, spouse, domestic partner, or such other individual is receiving care necessitated by a health condition or disability of the child, parent, spouse, domestic partner, or such other individual;\n**(C)**\nis in need of care and is typically cared for by an individual who is unable to provide care because the individual has any of the conditions or needs for diagnosis or care described in paragraph (1) or (2); or\n**(D)**\nis otherwise in need of care.\n**(4)**\nAn absence resulting from domestic violence, sexual assault, or stalking, if the time is to\u2014\n**(A)**\nseek medical attention for the employee or the employee\u2019s child, parent, spouse, domestic partner, or an individual related to the employee as described in paragraph (3), to recover from physical or psychological injury or disability caused by domestic violence, sexual assault, or stalking;\n**(B)**\nobtain or assist a child, a parent, a spouse, a domestic partner, or any other individual related by blood or affinity whose close association with the employee is the equivalent of a family relationship in obtaining services from a victim services organization;\n**(C)**\nobtain or assist a child, a parent, a spouse, a domestic partner, or any other individual related by blood or affinity whose close association with the employee is the equivalent of a family relationship in obtaining psychological or other counseling;\n**(D)**\nseek relocation; or\n**(E)**\ntake legal action, including preparing for or participating in any civil or criminal legal proceeding related to or resulting from domestic violence, sexual assault, or stalking.\n##### (c) Scheduling\nAn employee shall make a reasonable effort to schedule a period of paid sick time under this Act in a manner that does not unduly disrupt the operations of the employer.\n##### (d) Procedures\n**(1) In general**\nPaid sick time shall be provided upon the oral or written request of an employee. Such request shall\u2014\n**(A)**\ninclude the expected duration of the period of such time; and\n**(B)**\n**(i)**\nin a case in which the need for such period of time is foreseeable at least 7 days in advance of such period, be provided at least 7 days in advance of such period; or\n**(ii)**\notherwise, be provided as soon as practicable after the employee is aware of the need for such period.\n**(2) Certification in general**\n**(A) Provision**\n**(i) In general**\nSubject to subparagraph (C), an employer may require that a request for paid sick time under this section for a purpose described in paragraph (1), (2), or (3) of subsection (b) be supported by a certification issued by the health care provider of the eligible employee or of an individual described in subsection (b)(3), as appropriate, if the period of such time covers more than 3 consecutive workdays.\n**(ii) Timeliness**\nThe employee shall provide a copy of such certification to the employer in a timely manner, not later than 30 days after the first day of the period of time. The employer shall not delay the commencement of the period of time on the basis that the employer has not yet received the certification.\n**(B) Sufficient certification**\nA certification provided under subparagraph (A) shall be sufficient if it states\u2014\n**(i)**\nthe date on which the period of time will be needed;\n**(ii)**\nthe probable duration of the period of time; and\n**(iii)**\n**(I)**\nfor purposes of paid sick time under subsection (b)(1), a statement that absence from work is medically necessary;\n**(II)**\nfor purposes of such time under subsection (b)(2), the dates on which testing for a medical diagnosis or care is expected to be given and the duration of such testing or care; and\n**(III)**\nfor purposes of such time under subsection (b)(3), in the case of time to care for someone who is not a child, a statement that care is needed for an individual described in such subsection, and an estimate of the amount of time that such care is needed for such individual.\n**(C) Regulations**\nRegulations prescribed under section 12 shall specify the manner in which an employee who does not have health insurance shall provide a certification for purposes of this paragraph.\n**(D) Confidentiality and nondisclosure**\n**(i) Protected health information**\nNothing in this Act shall be construed to require a health care provider to disclose information in violation of section 1177 of the Social Security Act ( 42 U.S.C. 1320d\u20136 ) or the regulations promulgated pursuant to section 264(c) of the Health Insurance Portability and Accountability Act of 1996 ( 42 U.S.C. 1320d\u20132 note).\n**(ii) Health information records**\nIf an employer possesses health information about an employee or an employee\u2019s child, parent, spouse, domestic partner, or an individual related to the employee as described in subsection (b)(3), such information shall\u2014\n**(I)**\nbe maintained on a separate form and in a separate file from other personnel information;\n**(II)**\nbe treated as a confidential medical record; and\n**(III)**\nnot be disclosed except to the affected employee or with the permission of the affected employee.\n**(3) Certification in the case of domestic violence, sexual assault, or stalking**\n**(A) In general**\nAn employer may require that a request for paid sick time under this section for a purpose described in subsection (b)(4) be supported by a form of documentation described in subparagraph (B) if the period of such time covers more than 3 consecutive workdays.\n**(B) Form of documentation**\nA form of documentation described in this subparagraph is any one of the following:\n**(i)**\nA police report indicating that the employee, or an individual described in subsection (b)(4)(A) with respect to the employee, was a victim of domestic violence, sexual assault, or stalking.\n**(ii)**\nA court order protecting or separating the employee, or such an individual with respect to the employee, from the perpetrator of an act of domestic violence, sexual assault, or stalking, or other evidence from the court or prosecuting attorney that the employee, or an individual described in subsection (b)(4)(A) with respect to the employee, has appeared in court or is scheduled to appear in court in a proceeding related to domestic violence, sexual assault, or stalking.\n**(iii)**\nOther documentation signed by an employee or volunteer working for a victim services organization, an attorney, a police officer, a medical professional, a social worker, an antiviolence counselor, or a member of the clergy, affirming that the employee, or an individual described in subsection (b)(4)(A) with respect to the employee, is a victim of domestic violence, sexual assault, or stalking.\n**(C) Requirements**\nThe requirements of paragraph (2) shall apply to certifications under this paragraph, except that\u2014\n**(i)**\nsubparagraph (B)(iii) of such paragraph shall not apply;\n**(ii)**\nthe certification shall state the reason that the leave is required with the facts to be disclosed limited to the minimum necessary to establish a need for the employee to be absent from work, and the employee shall not be required to explain the details of the domestic violence, sexual assault, or stalking involved; and\n**(iii)**\nwith respect to confidentiality under subparagraph (D) of such paragraph, any information provided to the employer under this paragraph shall be confidential, except to the extent that any disclosure of such information is\u2014\n**(I)**\nrequested or consented to in writing by the employee; or\n**(II)**\notherwise required by applicable Federal or State law.\n**(D) Specification of documentation**\nAn employer may not specify which of the forms of documentation described in clause (i), (ii), or (iii) of subparagraph (B) is required to be provided in order to satisfy the requirement under subparagraph (A).\n#### 4. Notice requirement\n##### (a) In general\nEach employer shall notify each employee and include in any employee handbook, information\u2014\n**(1)**\ndescribing paid sick time available to employees under this Act;\n**(2)**\npertaining to the filing of an action under this Act;\n**(3)**\non the details of the notice requirement for a foreseeable period of time under section 3(d)(1)(B)(i); and\n**(4)**\nthat describes\u2014\n**(A)**\nthe protections that an employee has in exercising rights under this Act; and\n**(B)**\nhow the employee can contact the Secretary (or other appropriate authority as described in section 6) if any of the rights are violated.\n##### (b) Posting of notice\nEach employer shall post and keep posted a notice, to be prepared or approved in accordance with procedures specified in regulations prescribed under section 12, setting forth excerpts from, or summaries of, the pertinent provisions of this Act including the information described in paragraphs (1) through (4) of subsection (a).\n##### (c) Location\nThe notice described under subsection (b) shall be posted\u2014\n**(1)**\nin conspicuous places on the premises of the employer, where notices to employees (including applicants) are customarily posted; and\n**(2)**\nin employee handbooks.\n##### (d) Violation; penalty\nAny employer who willfully violates subsection (b) shall be subject to a civil fine in an amount not to exceed $100 for each separate offense.\n#### 5. Prohibited acts\n##### (a) Interference with rights\n**(1) Exercise of rights**\nIt shall be unlawful for any employer to interfere with, restrain, or deny the exercise of, or the attempt to exercise, any right provided under this Act, including\u2014\n**(A)**\ndischarging or discriminating against (including retaliating against) any individual, including a job applicant, for exercising, or attempting to exercise, any right provided under this Act;\n**(B)**\nusing the taking of paid sick time under this Act as a negative factor in an employment action, such as hiring, promotion, reducing hours or number of shifts, or a disciplinary action; or\n**(C)**\ncounting the paid sick time under a no-fault attendance policy or any other absence-control policy.\n**(2) Discrimination**\nIt shall be unlawful for any employer to discharge or in any other manner discriminate against (including retaliating against) any individual, including a job applicant, for opposing any practice made unlawful by this Act.\n##### (b) Interference with proceedings or inquiries\nIt shall be unlawful for any person to discharge or in any other manner discriminate against (including retaliating against) any individual, including a job applicant, because such individual\u2014\n**(1)**\nhas filed an action, or has instituted or caused to be instituted any proceeding, under or related to this Act;\n**(2)**\nhas given, or is about to give, any information in connection with any inquiry or proceeding relating to any right provided under this Act; or\n**(3)**\nhas testified, or is about to testify, in any inquiry or proceeding relating to any right provided under this Act.\n##### (c) Construction\nNothing in this section shall be construed to state or imply that the scope of the activities prohibited by section 105 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2615 ) is less than the scope of the activities prohibited by this section.\n#### 6. Enforcement authority\n##### (a) In general\n**(1) Definition**\nIn this subsection\u2014\n**(A)**\nthe term employee means an employee described in subparagraph (A) or (B) of section 2(5); and\n**(B)**\nthe term employer means an employer described in subclause (I) or (II) of section 2(6)(A)(i).\n**(2) Investigative authority**\n**(A) In general**\nTo ensure compliance with the provisions of this Act, or any regulation or order issued under this Act, the Secretary shall have, subject to subparagraph (C), the investigative authority provided under section 11(a) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 211(a) ), with respect to employers, employees, and other individuals affected by an employer.\n**(B) Obligation to keep and preserve records**\nAn employer shall make, keep, and preserve records pertaining to compliance with this Act in accordance with section 11(c) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 211(c) ) and in accordance with regulations prescribed by the Secretary.\n**(C) Required submissions generally limited to an annual basis**\nThe Secretary shall not require, under the authority of this paragraph, an employer to submit to the Secretary any books or records more than once during any 12-month period, unless the Secretary has reasonable cause to believe there may exist a violation of this Act or any regulation or order issued pursuant to this Act, or is investigating a charge pursuant to paragraph (4).\n**(D) Subpoena authority**\nFor the purposes of any investigation provided for in this paragraph, the Secretary shall have the subpoena authority provided for under section 9 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 209 ).\n**(3) Civil action by employees or individuals**\n**(A) Right of action**\nAn action to recover the damages or equitable relief prescribed in subparagraph (B) may be maintained against any employer in any Federal or State court of competent jurisdiction by an employee or individual or a representative for and on behalf of\u2014\n**(i)**\nthe employee or individual; or\n**(ii)**\nthe employee or individual and others similarly situated.\n**(B) Liability**\nAny employer who violates section 5 (including a violation relating to rights provided under section 3) shall be liable to any employee or individual affected\u2014\n**(i)**\nfor damages equal to\u2014\n**(I)**\nthe amount of\u2014\n**(aa)**\nany wages, salary, employment benefits, or other compensation denied or lost by reason of the violation; or\n**(bb)**\nin a case in which wages, salary, employment benefits, or other compensation have not been denied or lost, any actual monetary losses sustained as a direct result of the violation up to a sum equal to 56 hours of wages or salary for the employee or individual;\n**(II)**\nthe interest on the amount described in subclause (I) calculated at the prevailing rate; and\n**(III)**\nan additional amount as liquidated damages; and\n**(ii)**\nfor such equitable relief as may be appropriate, including employment, reinstatement, and promotion.\n**(C) Fees and costs**\nThe court in an action under this paragraph shall, in addition to any judgment awarded to the plaintiff, allow a reasonable attorney\u2019s fee, reasonable expert witness fees, and other costs of the action to be paid by the defendant.\n**(4) Action by the Secretary**\n**(A) Administrative action**\nThe Secretary shall receive, investigate, and attempt to resolve complaints of violations of section 5 (including a violation relating to rights provided under section 3) in the same manner that the Secretary receives, investigates, and attempts to resolve complaints of violations of sections 6 and 7 of the Fair Labor Standards Act of 1938 (29 U.S.C. 206 and 207).\n**(B) Civil action**\nThe Secretary may bring an action in any court of competent jurisdiction to recover the damages described in paragraph (3)(B)(i).\n**(C) Sums recovered**\nAny sums recovered by the Secretary pursuant to subparagraph (B) shall be held in a special deposit account and shall be paid, on order of the Secretary, directly to each employee or individual affected. Any such sums not paid to an employee or individual affected because of inability to do so within a period of 3 years shall be deposited into the Treasury of the United States as miscellaneous receipts.\n**(5) Limitation**\n**(A) In general**\nExcept as provided in subparagraph (B), an action may be brought under paragraph (3), (4), or (6) not later than 2 years after the date of the last event constituting the alleged violation for which the action is brought.\n**(B) Willful violation**\nIn the case of an action brought for a willful violation of section 5 (including a willful violation relating to rights provided under section 3), such action may be brought not later than 3 years after the last event constituting the alleged violation for which such action is brought.\n**(C) Commencement**\nIn determining when an action is commenced under paragraph (3), (4), or (6) for the purposes of this paragraph, it shall be considered to be commenced on the date when the complaint is filed.\n**(6) Action for injunction by Secretary**\nThe district courts of the United States shall have jurisdiction, for cause shown, in an action brought by the Secretary\u2014\n**(A)**\nto restrain violations of section 5 (including a violation relating to rights provided under section 3), including the restraint of any withholding of payment of wages, salary, employment benefits, or other compensation, plus interest, found by the court to be due to employees or individuals eligible under this Act; or\n**(B)**\nto award such other equitable relief as may be appropriate, including employment, reinstatement, and promotion.\n**(7) Solicitor of Labor**\nThe Solicitor of Labor may appear for and represent the Secretary on any litigation brought under paragraph (4) or (6).\n**(8) Government Accountability Office and Library of Congress**\nNotwithstanding any other provision of this subsection, in the case of the Government Accountability Office and the Library of Congress, the authority of the Secretary of Labor under this subsection shall be exercised respectively by the Comptroller General of the United States and the Librarian of Congress.\n##### (b) Employees covered by Congressional Accountability Act of 1995\nThe powers, remedies, and procedures provided in the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ) to the Board (as defined in section 101 of that Act ( 2 U.S.C. 1301 )), or any person, alleging a violation of section 202(a)(1) of that Act ( 2 U.S.C. 1312(a)(1) ) shall be the powers, remedies, and procedures this Act provides to that Board, or any person, alleging an unlawful employment practice in violation of this Act against an employee described in section 2(5)(C).\n##### (c) Employees covered by chapter 5 of title 3 , United States Code\nThe powers, remedies, and procedures provided in chapter 5 of title 3, United States Code, to the President, the Merit Systems Protection Board, or any person, alleging a violation of section 412(a)(1) of that title, shall be the powers, remedies, and procedures this Act provides to the President, that Board, or any person, respectively, alleging an unlawful employment practice in violation of this Act against an employee described in section 2(5)(D).\n##### (d) Employees covered by chapter 63 of title 5, United States Code\nThe powers, remedies, and procedures provided in title 5, United States Code, to an employing agency, provided in chapter 12 of that title to the Merit Systems Protection Board, or provided in that title to any person, alleging a violation of chapter 63 of that title, shall be the powers, remedies, and procedures this Act provides to that agency, that Board, or any person, respectively, alleging an unlawful employment practice in violation of this Act against an employee described in section 2(5)(E).\n##### (e) Remedies for State employees\n**(1) Waiver of sovereign immunity**\nA State\u2019s receipt or use of Federal financial assistance for any program or activity of a State shall constitute a waiver of sovereign immunity, under the 11th Amendment to the Constitution or otherwise, to a suit brought by an employee of that program or activity under this Act for equitable, legal, or other relief authorized under this Act.\n**(2) Official capacity**\nAn official of a State may be sued in the official capacity of the official by any employee who has complied with the procedures under subsection (a)(3), for injunctive relief that is authorized under this Act. In such a suit the court may award to the prevailing party those costs authorized by section 722 of the Revised Statutes ( 42 U.S.C. 1988 ).\n**(3) Applicability**\nWith respect to a particular program or activity, paragraph (1) applies to conduct occurring on or after the day, after the date of enactment of this Act, on which a State first receives or uses Federal financial assistance for that program or activity.\n**(4) Definition of program or activity**\nIn this subsection, the term program or activity has the meaning given the term in section 606 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d\u20134a ).\n#### 7. Education and outreach\n##### (a) In general\nThe Secretary may conduct a public awareness campaign to educate and inform the public of the requirements for paid sick time required by this Act.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary such sums as may be necessary to carry out such campaign.\n#### 8. Collection of data on paid sick time and further study\n##### (a) Compilation of information\nThe Commissioner of Labor Statistics of the Department of Labor shall annually compile and report to the Comptroller General of the United States information on\u2014\n**(1)**\nthe amount of paid sick time available to employees by occupation and type of employment establishment; and\n**(2)**\nan estimate of the average sick time used by employees according to occupation and the type of employment establishment.\n##### (b) GAO study\n**(1) In general**\nNot later than 5 years after the date of enactment of this Act, the Comptroller General of the United States shall conduct a study to evaluate the implementation of this Act. Such study shall include an estimation of employees\u2019 access to paid sick time, employees\u2019 awareness of their rights under this Act, and employers\u2019 experiences complying with this Act. Such study shall take into account access, awareness and experiences of employees by race, ethnicity, gender, and occupation.\n**(2) Report**\nUpon completion of the study required by paragraph (1), the Comptroller General of the United States shall prepare and submit a report to the appropriate committees of Congress concerning the results of the study and the information compiled pursuant to subsection (a).\n##### (c) Report on rail carrier enforcement\nNot later than 3 years after the date of enactment of this Act, the Secretary shall submit a report to Congress on any action by the Secretary under section 6(a) with respect to employers described in section 2(6)(B)(i)(IV) providing paid sick time to employees described in section 2(5)(A)(iii).\n#### 9. Effect on other laws\n##### (a) Federal and State antidiscrimination laws\nNothing in this Act shall be construed to modify or affect any Federal or State law prohibiting discrimination on the basis of race, religion, color, national origin, sex, age, disability, sexual orientation, gender identity, marital status, familial status, or any other protected status.\n##### (b) State and local laws\nNothing in this Act shall be construed to supersede (including preempting) any provision of any State or local law that provides greater paid sick time or leave rights (including greater amounts of paid sick time or leave or greater coverage of those eligible for paid sick time or leave) than the rights established under this Act.\n#### 10. Effect on existing employment benefits\n##### (a) More protective\nNothing in this Act shall be construed to diminish the obligation of an employer to comply with any contract, collective bargaining agreement, or any employment benefit program or plan that provides greater paid sick leave or other leave rights to employees or individuals than the rights established under this Act.\n##### (b) Less protective\nThe rights established for employees under this Act shall not be diminished by any contract, collective bargaining agreement, or any employment benefit program or plan.\n#### 11. Encouragement of more generous leave policies\nNothing in this Act shall be construed to discourage employers from adopting or retaining leave policies more generous than policies that comply with the requirements of this Act.\n#### 12. Regulations\n##### (a) In general\n**(1) Authority**\nExcept as provided in paragraph (2), not later than 180 days after the date of enactment of this Act, the Secretary shall prescribe such regulations as are necessary to carry out this Act with respect to employees described in subparagraph (A) or (B) of section 2(5) and other individuals affected by employers described in subclause (I) or (II) of section 2(6)(A)(i).\n**(2) Government Accountability Office; Library of Congress**\nThe Comptroller General of the United States and the Librarian of Congress shall prescribe the regulations with respect to employees of the Government Accountability Office and the Library of Congress, respectively, and other individuals affected by the Comptroller General of the United States and the Librarian of Congress, respectively.\n##### (b) Employees covered by Congressional Accountability Act of 1995\n**(1) Authority**\nNot later than 90 days after the Secretary prescribes regulations under subsection (a), the Board of Directors of the Office of Compliance shall prescribe (in accordance with section 304 of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1384 )) such regulations as are necessary to carry out this Act with respect to employees described in section 2(5)(C) and other individuals affected by employers described in section 2(6)(A)(i)(III).\n**(2) Agency regulations**\nThe regulations prescribed under paragraph (1) shall be the same as substantive regulations promulgated by the Secretary to carry out this Act except insofar as the Board may determine, for good cause shown and stated together with the regulations prescribed under paragraph (1), that a modification of such regulations would be more effective for the implementation of the rights and protections involved under this section.\n##### (c) Employees covered by chapter 5 of title 3 , United States Code\n**(1) Authority**\nNot later than 90 days after the Secretary prescribes regulations under subsection (a), the President (or the designee of the President) shall prescribe such regulations as are necessary to carry out this Act with respect to employees described in section 2(5)(D) and other individuals affected by employers described in section 2(6)(A)(i)(IV).\n**(2) Agency regulations**\nThe regulations prescribed under paragraph (1) shall be the same as substantive regulations promulgated by the Secretary to carry out this Act except insofar as the President (or designee) may determine, for good cause shown and stated together with the regulations prescribed under paragraph (1), that a modification of such regulations would be more effective for the implementation of the rights and protections involved under this section.\n##### (d) Employees covered by chapter 63 of title 5 , United States Code\n**(1) Authority**\nNot later than 90 days after the Secretary prescribes regulations under subsection (a), the Director of the Office of Personnel Management shall prescribe such regulations as are necessary to carry out this Act with respect to employees described in section 2(5)(E) and other individuals affected by employers described in section 2(6)(A)(i)(V).\n**(2) Agency regulations**\nThe regulations prescribed under paragraph (1) shall be the same as substantive regulations promulgated by the Secretary to carry out this Act except insofar as the Director may determine, for good cause shown and stated together with the regulations prescribed under paragraph (1), that a modification of such regulations would be more effective for the implementation of the rights and protections involved under this section.\n#### 13. Effective dates\n##### (a) Effective date\nThis Act shall take effect 6 months after the date of issuance of regulations under section 12(a)(1).\n##### (b) Collective bargaining agreements\nIn the case of a collective bargaining agreement in effect on the effective date prescribed by subsection (a), this Act shall take effect on the earlier of\u2014\n**(1)**\nthe date of the termination of such agreement;\n**(2)**\nthe date of any amendment, made on or after such effective date, to such agreement; or\n**(3)**\nthe date that occurs 18 months after the date of issuance of regulations under section 12(a)(1).",
      "versionDate": "2026-02-12",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-12",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7531",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Healthy Families Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2026-02-26T15:43:31Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3869is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Healthy Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthy Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow Americans to earn paid sick time so that they can address their own health needs and the health needs of their families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:29Z"
    }
  ]
}
```

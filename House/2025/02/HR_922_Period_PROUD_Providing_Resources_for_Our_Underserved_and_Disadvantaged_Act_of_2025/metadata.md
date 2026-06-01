# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/922?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/922
- Title: Period PROUD (Providing Resources for Our Underserved and Disadvantaged) Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 922
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-12-03T09:06:33Z
- Update date including text: 2025-12-03T09:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-04 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-04 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/922",
    "number": "922",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Period PROUD (Providing Resources for Our Underserved and Disadvantaged) Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-03T09:06:33Z",
    "updateDateIncludingText": "2025-12-03T09:06:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-02-04T17:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-04T17:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NM"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "DC"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "GA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "HI"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CT"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "GA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "TN"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "MD"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MI"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr922ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 922\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Casten (for himself, Ms. Meng , Ms. Stansbury , Ms. Vel\u00e1zquez , Ms. Dean of Pennsylvania , Mrs. Cherfilus-McCormick , Ms. Norton , Ms. Moore of Wisconsin , Ms. Sherrill , Mr. Grijalva , Mrs. Watson Coleman , Mr. Torres of New York , Mr. Meeks , Mr. Gottheimer , Mrs. McIver , Mr. Johnson of Georgia , Mr. Tonko , Ms. Jayapal , Ms. Wasserman Schultz , Ms. Clarke of New York , Ms. Tokuda , Mrs. Hayes , Mrs. McBath , Ms. Crockett , Ms. Budzinski , Ms. Schakowsky , Ms. Lee of Pennsylvania , and Mr. Garc\u00eda of Illinois ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide targeted funding for States and other eligible entities through the Social Services Block Grant program to increase the availability of menstrual products for individuals with limited access to such products.\n#### 1. Short title\nThis Act may be cited as the Period PROUD (Providing Resources for Our Underserved and Disadvantaged) Act of 2025 .\n#### 2. Targeted funding for menstrual products through the Social Services Block Grant Program\n##### (a) Increase in funding for Social Services Block Grant Program\n**(1) In general**\nThe amount specified in subsection (c) of section 2003 of the Social Security Act ( 42 U.S.C. 1397b ) for purposes of subsections (a) and (b) of such section is deemed to be $1,900,000,000 for each of fiscal years 2025 through 2028, of which the amount equal to $200,000,000, reduced by the amounts reserved under paragraph (2)(B) for each such fiscal year, shall be obligated by States in accordance with subsection (b).\n**(2) Appropriation**\n**(A) In general**\nOut of any money in the Treasury of the United States not otherwise appropriated, there is appropriated $200,000,000 for each of fiscal years 2026 through 2029, to carry out this section.\n**(B) Reservations**\n**(i) Purposes**\nThe Secretary shall reserve, from the amount appropriated under subparagraph (A) to carry out this section\u2014\n**(I)**\nfor each of fiscal years 2026 through 2029, not more than 2 percent of the amount appropriated for the fiscal year for purposes of entering into an agreement with an eligible entity described in subparagraph (C) to assist in providing technical assistance and training, to support effective policy, practice, research, and cross-system collaboration among grantees and subgrantees, and to assist in the administration of the program described in this section; and\n**(II)**\nfor fiscal year 2026, an amount, not to exceed $2,000,000, for purposes of conducting an evaluation under subsection (d).\n**(ii) No State entitlement to reserved funds**\nThe State entitlement under section 2002(a) of the Social Security Act ( 42 U.S.C. 1397a(a) ) shall not apply to the amounts reserved under clause (i).\n**(C) Eligible entity described**\nAn eligible entity described in this subparagraph is a nonprofit organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code, that\u2014\n**(i)**\nhas experience in the area of community distributions of basic need services, including experience collecting, warehousing, and distributing basic necessities such as menstrual products;\n**(ii)**\ndemonstrates competency to implement a project, provide fiscal accountability, collect data, and prepare reports and other necessary documentation; and\n**(iii)**\ndemonstrates a willingness to share information with researchers, practitioners, and other interested parties.\n##### (b) Rules governing use of additional funds\n**(1) In general**\nFunds are used in accordance with this subsection if\u2014\n**(A)**\nthe State, in consultation with relevant stakeholders, including agencies, professional associations, and nonprofit organizations, distributes the funds to eligible entities to\u2014\n**(i)**\ndecrease the unmet need for menstrual products by low-income menstruating individuals through\u2014\n**(I)**\nthe distribution of free menstrual products;\n**(II)**\ncommunity outreach to assist in participation in existing menstrual product distribution programs; or\n**(III)**\nimproving access to menstrual products among low-income individuals; and\n**(ii)**\nincrease the ability of communities and low-income families in such communities to provide for the need for menstrual products of low-income adults;\n**(B)**\nthe funds are used subject to the limitations in section 2005 of the Social Security Act ( 42 U.S.C. 1397d ); and\n**(C)**\nthe funds are used to supplement, and not supplant funds that are or have been made available from Federal, State, local, or philanthropic sources to carry out subtitle A of title XX of such Act.\n**(2) Allowable uses by eligible entities**\n**(A) In general**\nAn eligible entity receiving funds made available under subsection (a) shall use the funds for any of the following:\n**(i)**\nTo pay for the purchase of menstrual products by, and the distribution of menstrual products among low-income individuals.\n**(ii)**\nTo integrate activities carried out under subparagraph (A) with other basic needs assistance programs serving low-income families, including the following:\n**(I)**\nPrograms funded by the temporary assistance for needy families program under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ), including the State maintenance of effort provisions of such program.\n**(II)**\nPrograms designed to support the health of eligible children, such as the Children\u2019s Health Insurance Program under title XXI of the Social Security Act, the Medicaid program under title XIX of such Act, or State funded health care programs.\n**(III)**\nPrograms funded through the special supplemental nutrition program for women, infants, and children under section 17 of the Child Nutrition Act of 1966.\n**(IV)**\nPrograms that offer early home visiting services, including the maternal, infant, and early childhood home visiting program (including the Tribal home visiting program) under section 511 of the Social Security Act ( 42 U.S.C. 711 ).\n**(iii)**\nTo provide training or technical assistance in carrying out activities under this section.\n**(iv)**\nTo cover administrative costs.\n**(B) Limitation on use of funds for administrative costs**\nAn eligible entity receiving funds made available under this section shall not use more than 9 percent of the funds for administrative costs incurred pursuant to this section.\n**(C) No limits on where menstrual products may be distributed**\nThe Secretary may not limit the locations at which menstrual products may be distributed pursuant to this section.\n**(3) Availability of funds**\n**(A) Funds distributed to eligible entities**\nFunds made available under subsection (a) that are distributed to an eligible entity by a State for a fiscal year may be expended by the eligible entity only in such fiscal year or the succeeding fiscal year.\n**(B) Evaluation**\nFunds reserved under subsection (a)(2)(B)(i)(II) to carry out the evaluation under subsection (d) shall be available for expenditure through September 30, 2028.\n**(4) No effect on other programs**\nAny assistance or benefits received by a family through funds made available under subsection (a) shall be disregarded for purposes of determining the family\u2019s eligibility for, or amount of, benefits under any other Federal needs-based programs.\n##### (c) Annual reports\nSection 2004 of the Social Security Act shall apply with respect to payments made to a State under this section in the same way it applies with respect to payments made to a State under section 2002 of such Act.\n##### (d) Evaluation\nThe Secretary, in consultation with States and the eligible entities described in subsection (a)(2)(C) receiving funds made available under this section, shall\u2014\n**(1)**\nnot later than December 30, 2031, complete an evaluation of the effectiveness of the assistance program carried out pursuant to this section, such as the effect of activities carried out under this Act on mitigating the health risks of unmet menstrual products need among individuals in low-income families;\n**(2)**\nnot later than March 31, 2032, submit to the Committees on Energy and Commerce and on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a report on the results of the evaluation; and\n**(3)**\nnot later than April 30, 2032, publish the results of the evaluation on the internet website of the Department of Health and Human Services.\n##### (e) Guidance\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall issue guidance regarding how the provisions of this section should be carried out, including information regarding eligible entities, allowable use of funds, and reporting requirements.\n##### (f) Definitions\nIn this section:\n**(1) Menstrual products**\nThe term menstrual products means menstrual cups, menstrual discs, menstrual underwear, and sanitary napkins and tampons, that conform to applicable industry standards.\n**(2) Eligible entities**\nThe term eligible entity means a State or local governmental entity, an Indian tribe or tribal organization (as defined in section 4 of the Indian Self-Determination and Education Assistance Act), or a nonprofit organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code that\u2014\n**(A)**\nhas experience in the area of community distributions of basic need services, including experience collecting, warehousing, and distributing basic necessities such as diapers, food, or menstrual products;\n**(B)**\ndemonstrates competency to implement a project, provide fiscal accountability, collect data, and prepare reports and other necessary documentation; and\n**(C)**\ndemonstrates a willingness to share information with researchers, practitioners, and other interested parties.\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(4) State**\nThe term State has the meaning given in section 1101(a)(1) of the Social Security Act for purposes of title XX of such Act.\n##### (g) Limitation on authorization of appropriations\nFor the administration of this section, there are authorized to be appropriated to the Secretary not more than $6,000,000 for fiscal years 2026 through 2029.\n##### (h) Exemption from sequestration\nFunds made available to carry out this section shall be exempt from reduction under any order issued under the Balanced Budget and Emergency Deficit Control Act of 1985.",
      "versionDate": "2025-02-04",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-05-29",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on the Judiciary, Financial Services, Energy and Commerce, Transportation and Infrastructure, Ways and Means, and the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3644",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Menstrual Equity For All Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Appropriations",
            "updateDate": "2025-06-09T16:51:34Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-09T16:51:50Z"
          },
          {
            "name": "Cosmetics and personal care",
            "updateDate": "2025-06-09T16:51:56Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-06-09T16:51:38Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-09T16:51:43Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-06-09T16:52:03Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-06-09T16:51:29Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-06-09T16:52:09Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-06-09T16:51:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-02T15:26:11Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr922ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Period PROUD (Providing Resources for Our Underserved and Disadvantaged) Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Period PROUD (Providing Resources for Our Underserved and Disadvantaged) Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide targeted funding for States and other eligible entities through the Social Services Block Grant program to increase the availability of menstrual products for individuals with limited access to such products.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:19Z"
    }
  ]
}
```

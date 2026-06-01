# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2702?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2702
- Title: FIRM Act
- Congress: 119
- Bill type: HR
- Bill number: 2702
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 19.
- 2025-06-20 - Calendars: Placed on the Union Calendar, Calendar No. 131.
- 2025-06-20 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-164.
- 2025-06-20 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-164.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 19.
- 2025-06-20 - Calendars: Placed on the Union Calendar, Calendar No. 131.
- 2025-06-20 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-164.
- 2025-06-20 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-164.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2702",
    "number": "2702",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "FIRM Act",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-06-20",
      "calendarNumber": {
        "calendar": "U00131"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 131.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-06-20",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-164.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-06-20",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-164.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 19.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
        "item": [
          {
            "date": "2025-06-20T15:00:01Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-21T16:04:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-08T14:05:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "MI"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "OK"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "GA"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "TN"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "MO"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "IN"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "SC"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "WI"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "NC"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "IN"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "TN"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "MT"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "TX"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "WI"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "TX"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "KS"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2702ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2702\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Barr (for himself, Mr. Torres of New York , Mrs. McClain , Mr. Lucas , Mr. Loudermilk , Mr. Rose , Mrs. Wagner , Mr. Stutzman , Mr. Timmons , Mr. Fitzgerald , Mr. Moore of North Carolina , Mr. Messmer , Mr. Ogles , Mr. Downing , Mr. Sessions , Mr. LaMalfa , and Mr. Grothman ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo curtail the political weaponization of Federal banking agencies by eliminating reputational risk as a component of the supervision of depository institutions.\n#### 1. Short title\nThis Act may be cited as the Financial Integrity and Regulation Management Act or the FIRM Act .\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe primary objective of financial regulation and supervision by the Federal banking agencies is to promote safety and soundness of depository institutions;\n**(2)**\nall federally legal businesses and law-abiding citizens regardless of political ideology should have equal opportunity to obtain financial services and should not face unlawful discrimination in obtaining such services;\n**(3)**\nfinancial service providers are private entities entitled to provide services to whichever customers they so choose, provided that those decisions do not violate the law;\n**(4)**\nfinancial service providers should strive to ensure that all business decisions are based on factors free from unlawful prejudice or political influence;\n**(5)**\nthe use of reputational risk in supervisory frameworks encourages Federal banking agencies to regulate depository institutions based on the subjective view of negative publicity and provides cover for the agencies to implement their own political agenda unrelated to the safety and soundness of a depository institution;\n**(6)**\nFederal banking agencies have in fact used reputational risk to limit access of federally legal businesses and law-abiding citizens to financial services in 2018 when the Federal Deposit Insurance Corporation acknowledged that the agency used reputational risk reviews to limit access to financial services by certain industries, commonly known as Operation Choke Point ; and\n**(7)**\nreputational risk does not appear in any statute and is an unnecessary and improper use of supervisory authority that does not contribute to the safety and soundness of the financial system.\n#### 3. Definitions\nIn this Act:\n**(1) Depository institution**\nThe term depository institution \u2014\n**(A)**\nhas the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nincludes an insured credit union.\n**(2) Federal banking agency**\nThe term Federal banking agency \u2014\n**(A)**\nhas the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nincludes\u2014\n**(i)**\nthe National Credit Union Administration; and\n**(ii)**\nthe Bureau of Consumer Financial Protection.\n**(3) Insured credit union**\nThe term insured credit union has the meaning given the term in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) Reputational risk**\nThe term reputational risk means the potential that negative publicity or negative public opinion regarding an institution\u2019s business practices, whether true or not, will cause a decline in confidence in the institution or a decline in the customer base, costly litigation, or revenue reductions or otherwise adversely impact the depository institution.\n#### 4. Removal of reputational risk as a consideration in the supervision of depository institutions\nEach Federal banking agency shall remove from any guidance, rule, examination manual, or similar document established by the agency any reference to reputational risk, or any term substantially similar, regarding the supervision of depository institutions such that reputational risk, or any term substantially similar, is no longer taken into consideration by the Federal banking agency when examining and supervising a depository institution.\n#### 5. Prohibition\nNo Federal banking agency may engage in any activity concerning or related to the regulation, supervision, or examination, of the reputational risk, or any term substantially similar, or the management thereof, of a depository institution, including\u2014\n**(1)**\nestablishing any rule, regulation, requirement, standard, or supervisory expectation concerning or related to the reputational risk, or any term substantially similar, or the management thereof, of a depository institution whether binding or not;\n**(2)**\nconducting any examination, assessment, data collection, or other supervisory exercise concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution;\n**(3)**\nissuing any examination finding, supervisory criticism, or other supervisory or examination communication concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution;\n**(4)**\nmaking any supervisory ratings decision or determination that is based, in whole or in part, on any matter concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution; and\n**(5)**\ntaking any formal or informal enforcement action that is based, in whole or in part, on any matter concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution.\n#### 6. Reports\nNot later than 180 days after the date of enactment of this Act, each Federal banking agency shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report that\u2014\n**(1)**\nconfirms implementation of this Act; and\n**(2)**\ndescribes any changes made to internal policies as a result of this Act.",
      "versionDate": "2025-04-08",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2702rh.xml",
      "text": "IB\nUnion Calendar No. 131\n119th CONGRESS\n1st Session\nH. R. 2702\n[Report No. 119\u2013164]\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Barr (for himself, Mr. Torres of New York , Mrs. McClain , Mr. Lucas , Mr. Loudermilk , Mr. Rose , Mrs. Wagner , Mr. Stutzman , Mr. Timmons , Mr. Fitzgerald , Mr. Moore of North Carolina , Mr. Messmer , Mr. Ogles , Mr. Downing , Mr. Sessions , Mr. LaMalfa , and Mr. Grothman ) introduced the following bill; which was referred to the Committee on Financial Services\nJune 20, 2025 Additional sponsors: Mr. Williams of Texas , Mr. Schmidt , and Mr. Garbarino\nJune 20, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on April 8, 2025\nA BILL\nTo curtail the political weaponization of Federal banking agencies by eliminating reputational risk as a component of the supervision of depository institutions.\n#### 1. Short title\nThis Act may be cited as the Financial Integrity and Regulation Management Act or the FIRM Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe primary objective of financial regulation and supervision by the Federal banking agencies is to promote safety and soundness of depository institutions;\n**(2)**\nall federally legal businesses and law-abiding citizens regardless of political ideology should have equal opportunity to obtain financial services and should not face unlawful discrimination in obtaining such services;\n**(3)**\nfinancial service providers are private entities entitled to provide services to whichever customers they so choose, provided that those decisions do not violate the law;\n**(4)**\nfinancial service providers should strive to ensure that all business decisions are based on factors free from unlawful prejudice or political influence;\n**(5)**\nthe use of reputational risk in supervisory frameworks encourages Federal banking agencies to regulate depository institutions based on the subjective view of negative publicity and provides cover for the agencies to implement their own political agenda unrelated to the safety and soundness of a depository institution;\n**(6)**\nFederal banking agencies have in fact used reputational risk to limit access of federally legal businesses and law-abiding citizens to financial services in 2018 when the Federal Deposit Insurance Corporation acknowledged that the agency used reputational risk reviews to limit access to financial services by certain industries, commonly known as Operation Choke Point ; and\n**(7)**\nreputational risk does not appear in any statute and is an unnecessary and improper use of supervisory authority that does not contribute to the safety and soundness of the financial system.\n#### 3. Definitions\nIn this Act:\n**(1) Depository institution**\nThe term depository institution \u2014\n**(A)**\nhas the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nincludes an insured credit union, as such term is defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(2) Federal banking agency**\nThe term Federal banking agency \u2014\n**(A)**\nhas the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nincludes\u2014\n**(i)**\nthe National Credit Union Administration; and\n**(ii)**\nthe Bureau of Consumer Financial Protection.\n**(3) Foreign terrorist organization**\nThe term foreign terrorist organization means a foreign organization that is designated by the Secretary of State in accordance with section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).\n**(4) Reputational risk**\nThe term reputational risk means the potential that negative publicity or negative public opinion regarding a depository institution\u2019s business practices, whether true or not, will cause a decline in confidence in the institution or a decline in the customer base, costly litigation, or revenue reductions or otherwise adversely impact the depository institution. The previous sentence does not apply to negative publicity or negative public opinion regarding an institution\u2019s business practices where such practices involve unlawful transactions in connection with state sponsors of terrorism or foreign terrorist organizations.\n**(5) State sponsors of terrorism**\nThe term state sponsors of terrorism means a country, the government of which has been determined by the Secretary of State to have repeatedly provided support for acts of international terrorism, for purposes of\u2014\n**(A)**\nsection 1754(c)(1)(A)(i) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A)(i) );\n**(B)**\nsection 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 );\n**(C)**\nsection 40(d) of the Arms Export Control Act ( 22 U.S.C. 2780(d) ); or\n**(D)**\nany other provision of law.\n#### 4. Removal of reputational risk as a consideration in the supervision of depository institutions\nEach Federal banking agency shall remove from any guidance, rule, examination manual, or similar document established by the agency any reference to reputational risk, or any term substantially similar, regarding the supervision of depository institutions such that reputational risk, or any term substantially similar, is no longer taken into consideration by the Federal banking agency when examining and supervising a depository institution.\n#### 5. Prohibition\nNo Federal banking agency may engage in any activity concerning or related to the regulation, supervision, or examination of the reputational risk, or any term substantially similar, or the management thereof, of a depository institution, including\u2014\n**(1)**\nestablishing any rule, regulation, requirement, standard, or supervisory expectation concerning or related to the reputational risk, or any term substantially similar, or the management thereof, of a depository institution whether binding or not;\n**(2)**\nconducting any examination, assessment, data collection, or other supervisory exercise concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution;\n**(3)**\nissuing any examination finding, supervisory criticism, or other supervisory or examination communication concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution;\n**(4)**\nmaking any supervisory ratings decision or determination that is based, in whole or in part, on any matter concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution; and\n**(5)**\ntaking any formal or informal enforcement action that is based, in whole or in part, on any matter concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution.\n#### 6. Reports\nNot later than 180 days after the date of enactment of this Act, each Federal banking agency shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report that\u2014\n**(1)**\nconfirms implementation of this Act; and\n**(2)**\ndescribes any changes made to internal policies as a result of this Act.",
      "versionDate": "2025-06-20",
      "versionType": "Reported in House"
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
        "actionDate": "2026-04-20",
        "text": "Placed on the Union Calendar, Calendar No. 535."
      },
      "number": "6955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-18",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 32."
      },
      "number": "875",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FIRM Act",
      "type": "S"
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-05-28T15:20:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-28T15:20:53Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-05-28T15:20:53Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-28T15:20:53Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-28T15:20:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-02T13:22:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-08",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2702",
          "measure-number": "2702",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-08",
          "originChamber": "HOUSE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2702v00",
            "update-date": "2026-04-13"
          },
          "action-date": "2025-04-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Financial Integrity and Regulation Management Act or the FIRM Act</strong></p><p>This bill prohibits the consideration of\u00a0reputational risk by federal banking agencies when regulating, examining, or supervising a depository institution or credit union. The bill defines <em>reputational risk</em> as the potential for negative publicity or public attention to decrease confidence in the institution, lead to litigation, reduce revenues, or result in other adverse impacts to the institution.\u00a0</p><p>Agencies must report on the implementation of this bill.\u00a0</p>"
        },
        "title": "FIRM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2702.xml",
    "summary": {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Financial Integrity and Regulation Management Act or the FIRM Act</strong></p><p>This bill prohibits the consideration of\u00a0reputational risk by federal banking agencies when regulating, examining, or supervising a depository institution or credit union. The bill defines <em>reputational risk</em> as the potential for negative publicity or public attention to decrease confidence in the institution, lead to litigation, reduce revenues, or result in other adverse impacts to the institution.\u00a0</p><p>Agencies must report on the implementation of this bill.\u00a0</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr2702"
    },
    "title": "FIRM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Financial Integrity and Regulation Management Act or the FIRM Act</strong></p><p>This bill prohibits the consideration of\u00a0reputational risk by federal banking agencies when regulating, examining, or supervising a depository institution or credit union. The bill defines <em>reputational risk</em> as the potential for negative publicity or public attention to decrease confidence in the institution, lead to litigation, reduce revenues, or result in other adverse impacts to the institution.\u00a0</p><p>Agencies must report on the implementation of this bill.\u00a0</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr2702"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2702ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2702rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "FIRM Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-06-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Financial Integrity and Regulation Management Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-06-21T03:53:17Z"
    },
    {
      "title": "FIRM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T03:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIRM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Financial Integrity and Regulation Management Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To curtail the political weaponization of Federal banking agencies by eliminating reputational risk as a component of the supervision of depository institutions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T03:33:24Z"
    }
  ]
}
```

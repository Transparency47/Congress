# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4199?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4199
- Title: Modernize the Au Pair Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4199
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-05-01T08:08:50Z
- Update date including text: 2026-05-01T08:08:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4199",
    "number": "4199",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000610",
        "district": "14",
        "firstName": "Guy",
        "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
        "lastName": "Reschenthaler",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Modernize the Au Pair Program Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:50Z",
    "updateDateIncludingText": "2026-05-01T08:08:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "FL"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "WA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "WI"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4199ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4199\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Reschenthaler (for himself, Ms. Salazar , and Mr. Issa ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo clarify the Department of State\u2019s exclusive regulatory authority over the au pair cultural exchange program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernize the Au Pair Program Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress authorized in the Mutual Educational and Cultural Exchange Act of 1961, (22 U.S.C. 2451 et. seq. (known as the Fulbright-Hays Act )) the creation of international educational and cultural exchange programs pursued through private-public partnerships between the Federal agency responsible for foreign affairs (initially the United States Information Agency or USIA ) and designated sponsoring organizations.\n**(2)**\nIn 1986, the USIA launched a pilot program referred to as the Federal au pair exchange program , whereby young foreign students would travel to the United States to live with and provide childcare to an American family, immerse themselves in American culture, and pursue academic credits at an accredited institution.\n**(3)**\nIn 1994, Congress amended the Eisenhower Exchange Fellowship Act of 1990 ( Public Law 103\u2013415 , 108 Stat. 4299 (1994)) to clarify that the USIA should continue to administer the Federal au pair program consistent with foreign affairs purposes of the Fulbright-Hays Act.\n**(4)**\nThe USIA exercised its regulatory authority over the program to promulgate comprehensive regulations that set requirements for the educational component of the program, specified the eligibility criteria for au pairs, and crafted a nationally uniform weekly stipend formula for host families to provide to their au pairs that was based on an assumed number of weekly hours of childcare, indexed on the Federal minimum wage, and reflected a 40 percent credit for the provided room and board.\n**(5)**\nIn 1997, Congress authorized the Federal au pair program on a permanent basis ( Public Law 105\u201348 , 111 Stat. 1165 (1997)).\n**(6)**\nIn 1999, the USIA disbanded and Congress transferred regulatory authority for the au pair program to the Department of State.\n**(7)**\nThe au pair program is an important public diplomacy tool that furthers foreign policy objectives of the United States.\n**(8)**\nThe au pair program provides a critical source of affordable childcare for tens of thousands of American families at a time when the lack of access to such care costs the economy of the United States an estimated $122,000,000,000 annually in lost earnings, productivity, and revenue.\n**(9)**\nStudies have shown that over 10 percent of au pair host families are active duty military personnel, and additionally the au pair program has become an essential source of childcare for families of first responders, single parents, and shift workers and others with non-traditional work schedules.\n**(10)**\nAny and all Federal regulations pertaining to the au pair program must retain the national uniformity and affordability integral to allowing American working families to continue their participation in the program.\n**(11)**\nAmerican families participating in the au pair program must have clarity and confidence in what laws and regulations are applicable to the program.\n**(12)**\nIt is clear that, consistent with congressional intent, the au pair program must be exclusively regulated by Federal law to successfully serve a foreign affairs purpose.\n#### 3. Clarification of exclusive Federal regulatory authority\nA State or political subdivision of a State may not enact or enforce a law, regulation, or other provision having the force or effect of law related to the au pair program administered by the Department of State.\n#### 4. Revised proposed rule on au pair program\nNot later than 90 days after the date of enactment of this Act, the Secretary of State shall submit to the Director of the Office of Management and Budget a proposed rule that shall\u2014\n**(1)**\nprovide a uniform national modification to the stipend and the educational stipend provided by a host family to an au pair, in a manner that does not make the program prohibitively expensive for and reflects the room, board, and other programmatic costs borne by a host family;\n**(2)**\nenhance flexibility in the au pair program, to accommodate unique work and family scheduling needs of military families, first responders, single parents, shift workers, and other host families with non-traditional work schedules; and\n**(3)**\npromote the immersion of an au pair into the family life of their host family, consistent with the cultural exchange purposes of the au pair program.",
      "versionDate": "2025-06-26",
      "versionType": "Introduced in House"
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
        "name": "International Affairs",
        "updateDate": "2025-07-24T19:08:43Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4199ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To clarify the Department of State's exclusive regulatory authority over the au pair cultural exchange program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T06:08:43Z"
    },
    {
      "title": "Modernize the Au Pair Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T06:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modernize the Au Pair Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-17T06:08:21Z"
    }
  ]
}
```

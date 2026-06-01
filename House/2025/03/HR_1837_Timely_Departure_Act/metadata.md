# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1837?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1837
- Title: Timely Departure Act
- Congress: 119
- Bill type: HR
- Bill number: 1837
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2025-11-20T09:06:16Z
- Update date including text: 2025-11-20T09:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1837",
    "number": "1837",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "O000177",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Onder, Robert [R-MO-3]",
        "lastName": "Onder",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Timely Departure Act",
    "type": "HR",
    "updateDate": "2025-11-20T09:06:16Z",
    "updateDateIncludingText": "2025-11-20T09:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "AL"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "MD"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "FL"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1837ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1837\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mr. Onder (for himself, Mr. Moore of Alabama , Mr. Nehls , Mr. Gill of Texas , Mr. Harris of Maryland , Mr. Haridopolos , and Mr. Harris of North Carolina ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require aliens seeking admission to the United States as nonimmigrants to pay a bond or cash payment and to impose penalties on such aliens who fail to timely depart the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Timely Departure Act .\n#### 2. Visa overstay bonds and penalties\n##### (a) Definitions\nIn this Act:\n**(1) In general**\nA term used in this section that is used in the immigration laws shall have the meaning given such term in the immigration laws.\n**(2) Immigration laws**\nThe term immigration laws has the meaning given such term under section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ).\n##### (b) Nonimmigrant bonds\n**(1) Admission contingent on posting of bond**\n**(A) In general**\nExcept as provided in subparagraph (B), an alien seeking admission to the United States as a nonimmigrant shall pay a bond or cash payment in an amount not less than $5,000 and not more than $50,000 to help ensure that the alien departs the United States before the date on which his or her period of stay authorized by the Secretary of Homeland Security in connection with such status expires.\n**(B) Nonapplicability to certain aliens**\nSubparagraph (A) shall not apply to any alien who\u2014\n**(i)**\nis present in the United States pursuant to a nonimmigrant visa issued under subparagraph (A), (C), (G), (P)(i), (T), or (U) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ); or\n**(ii)**\nis a national of a program country for purposes of the visa waiver program under section 217 of the Immigration and Nationality Act ( 8 U.S.C. 1187 ).\n**(2) Automatic and nonappealable forfeiture**\n**(A) In general**\nIn the case of a nonimmigrant who has paid a bond or cash payment under paragraph (1) who fails to depart the United States before midnight (Pacific Time) on the date on which his or her authorized period of stay expires, such bond or cash payment shall be forfeited without the opportunity for appeal or review.\n**(B) Offsetting account**\nA forfeited bond or cash payment under this paragraph shall be deposited in an offsetting account under the jurisdiction of the Secretary of Homeland Security, to be known as the Immigration Detention and Enforcement Account , and the amounts deposited into such account shall be used solely for purposes of funding alien detention facilities and international transportation for aliens ordered removed from the United States.\n**(3) Removal and immigration penalty**\nAn alien whose bond or cash payment is forfeited under paragraph (2) shall be\u2014\n**(A)**\npromptly removed from the United States; and\n**(B)**\nfor a period not less than 4 years and not more than 12 years beginning on the date of such forfeiture, ineligible for any lawful immigration status or adjustment of status under the immigration laws.\n##### (c) Limitation on asylum and withholding of removal claims\n**(1) In general**\nAn alien present in the United States pursuant to admission as a nonimmigrant who intends to seek asylum or withholding of removal in the United States shall submit an application for asylum or withholding of removal before midnight (Pacific Time) on the date on which his or her authorized period of stay in connection with nonimmigrant status expires.\n**(2) Consequence of failure to timely depart**\nAn alien described in paragraph (1) who fails to depart the United States before midnight (Pacific Time) on the date on which his or her authorized period of stay expires and who has not submitted an application for asylum or withholding of removal shall be ineligible to submit such an application after such date.\n##### (d) Regulations\n**(1) In general**\nIn implementing this section, the Secretary of Homeland Security may only issue regulations or policy guidance with respect to\u2014\n**(A)**\nthe collection and retention of bonds and cash payments;\n**(B)**\nthe notification of the Attorney General with respect to the failure of an alien to timely depart the United States before midnight (Pacific Time) on the date on which his or her authorized period of stay in connection with nonimmigrant status expires; and\n**(C)**\nthe prevention of the circumvention of the requirement to pay a bond or cash payment under subsection (b)(1).\n**(2) Prohibition**\nThe Secretary of Homeland Security shall not waive or nullify any requirement of this section, whether by rulemaking, order, or other action.\n##### (e) Effective date\nThis section shall take effect on the date that is 30 days after the date of the enactment of this Act.",
      "versionDate": "2025-03-04",
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
        "name": "Immigration",
        "updateDate": "2025-03-19T13:23:56Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1837ih.xml"
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
      "title": "Timely Departure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T09:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Timely Departure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require aliens seeking admission to the United States as nonimmigrants to pay a bond or cash payment and to impose penalties on such aliens who fail to timely depart the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T09:48:24Z"
    }
  ]
}
```

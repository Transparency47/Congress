# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6707?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6707
- Title: CFIUSMCA Act
- Congress: 119
- Bill type: HR
- Bill number: 6707
- Origin chamber: House
- Introduced date: 2025-12-15
- Update date: 2026-04-20T15:14:49Z
- Update date including text: 2026-04-20T15:14:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-15: Introduced in House

## Actions

- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6707",
    "number": "6707",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "CFIUSMCA Act",
    "type": "HR",
    "updateDate": "2026-04-20T15:14:49Z",
    "updateDateIncludingText": "2026-04-20T15:14:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T17:01:15Z",
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
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "IL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "MI"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6707ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6707\nIN THE HOUSE OF REPRESENTATIVES\nDecember 15, 2025 Mr. Arrington (for himself, Mr. Schneider , Mr. Moran , and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo direct the United States Trade Representative to prioritize North American alignment on foreign investment review during the next joint review conducted under the United States-Mexico-Canada Agreement.\n#### 1. Short title\nThis Act may be cited as the Consistency in Foreign Investment in the United States-Mexico-Canada Agreement Act or the CFIUSMCA Act .\n#### 2. North American alignment on foreign investment review\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nCanada and Mexico are the two largest trading partners of the United States, with bilateral goods and services trade between the United States and each such country reaching approximately $1,000,000,000,000 in 2024;\n**(2)**\nthe United States-Mexico-Canada Agreement (USMCA) underpins much of the trade referred to in paragraph (1) and promotes a strong North American supply chain that supports millions of good-paying jobs in the United States;\n**(3)**\ngiven the close economic relationship between the United States, Mexico, and Canada under the USMCA, ensuring that each party has robust investment review mechanisms in place is important towards strengthening the collective national security interests of those countries;\n**(4)**\nthe Committee on Foreign Investment in the United States plays a critical role in protecting the national security of the United States by reviewing foreign investments for national security risks; and\n**(5)**\nthe establishment or modification by Mexico and Canada of legislative and regulatory frameworks to review foreign investments for national security risks that are similar to the framework established under section 721 of the Defense Production Act of 1950 ( 50 U.S.C. 4565 ) would\u2014\n**(A)**\nadvance the national security interests of the United States; and\n**(B)**\nallow for closer coordination between the USMCA countries with respect to shared threats from investments in strategically important economic sectors and critical infrastructure in North America.\n##### (b) Joint review negotiation objective\nSubject to the requirements of section 611 of the United States-Mexico-Canada Agreement Implementation Act ( 19 U.S.C. 4611 ), during the first joint review conducted after the date of the enactment of this Act, the Trade Representative shall advocate for\u2014\n**(1)**\neach USMCA country to implement a legislative and regulatory framework for reviewing foreign investment for national security risks that is similar to the framework established under section 721 of the Defense Production Act of 1950 ( 50 U.S.C. 4565 ); and\n**(2)**\nthe establishment of a mechanism for USMCA countries to coordinate to address shared threats from investments in strategically important economic sectors and critical infrastructure in North America that is overseen by the Trade Representative, Secretary of State, and Secretary of the Treasury and provides a forum for each USMCA country to\u2014\n**(A)**\nimplement this mechanism;\n**(B)**\nenhance communication and cooperation among the USMCA countries related to shared threats from foreign investment;\n**(C)**\nfacilitate the development of consistent foreign investment screening practices and standards among the USMCA countries;\n**(D)**\nexchange information on shared threats from investments in strategically important economic sectors and critical infrastructure;\n**(E)**\nnotify the other USMCA countries of investments in strategically important economic sectors and critical infrastructure; and\n**(F)**\nidentify, consult, manage, and resolve existing or proposed foreign investments in one USMCA country determined to pose a national security risk to another USMCA country.\n##### (c) Technical assistance\nIn carrying out subsection (b)(1), the Trade Representative shall coordinate with the Secretary of the Treasury and the Secretary of State with respect to the provision of technical assistance to USMCA countries to support the establishment or modification of frameworks for reviewing foreign investments for national security risks. With respect to the provision of technical assistance to USMCA countries to support the establishment or modification of frameworks for reviewing foreign investment for national security risks, the Trade Representative shall also consult closely and on a timely basis with appropriate Congressional committees, including the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate.\n##### (d) Definitions\nIn this section:\n**(1) Critical infrastructure**\nThe term critical infrastructure means, in the context of a particular covered control transaction, systems and assets, whether physical or virtual, so vital to the United States that the incapacity or destruction of such systems or assets would have a debilitating impact on national security.\n**(2) Foreign investment**\nThe term foreign investment has the meaning given the terms covered investment , covered investment critical infrastructure , and covered transaction in sections 800.211 through 800.213 of title 31, Code of Federal Regulations.\n**(3) Joint review**\nThe term joint review has the meaning given that term in section 611 of the United States-Mexico-Canada Agreement Implementation Act ( 19 U.S.C. 4611 ).\n**(4) Trade Representative**\nThe term Trade Representative means the United States Trade Representative.\n**(5) National security risk**\nThe term national security risk has the meaning given that term for purposes of any determination under section 721 of the Defense Production Act of 1950, including as provided in Executive Order 14083 (87 Fed. Reg. 57369; relating to ensuring robust consideration of evolving national security risks by the Committee on Foreign Investment in the United States).\n**(6) Strategically important economic sectors**\nThe term strategically important economic sectors includes\u2014\n**(A)**\nadvanced computing;\n**(B)**\nadvanced engineering materials;\n**(C)**\nadvanced gas turbine engine technologies;\n**(D)**\nadvanced and networked sensing and signature management;\n**(E)**\nadvanced manufacturing;\n**(F)**\nartificial intelligence;\n**(G)**\nbiotechnologies;\n**(H)**\ncritical technologies, as such term is defined in section 800.215 of title 31, Code of Federal Regulations;\n**(I)**\ndata privacy, data security, and cybersecurity technologies;\n**(J)**\ndirected energy;\n**(K)**\nhighly automated, autonomous, and uncrewed systems, and robotics;\n**(L)**\nhuman-machine interfaces;\n**(M)**\nhypersonics;\n**(N)**\nintegrated communication and networking technologies;\n**(O)**\npositioning, navigation, and timing technologies;\n**(P)**\nquantum information and enabling technologies;\n**(Q)**\nsemiconductors and microelectronics; and\n**(R)**\nspace technologies and systems.\n**(7) USMCA**\nThe term USMCA has the meaning given that term in section 3 of the United States-Mexico-Canada Agreement Implementation Act ( 19 U.S.C. 4502 ).\n**(8) USMCA country**\nThe term USMCA country has the meaning given that term in section 202(a) of the United States-Mexico-Canada Agreement Implementation Act ( 19 U.S.C. 4531(a) ).",
      "versionDate": "2025-12-15",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-04-20T15:14:49Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6707ih.xml"
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
      "title": "CFIUSMCA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CFIUSMCA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Consistency in Foreign Investment in the United States-Mexico-Canada Agreement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the United States Trade Representative to prioritize North American alignment on foreign investment review during the next joint review conducted under the United States-Mexico-Canada Agreement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:24Z"
    }
  ]
}
```

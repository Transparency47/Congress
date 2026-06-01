# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/929?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/929
- Title: GATE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 929
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/929",
    "number": "929",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "GATE Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T15:58:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "UT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "ME"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "WY"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "OK"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "ID"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s929is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 929\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Cotton (for himself, Mr. Lee , Ms. Collins , Mr. Barrasso , Mr. Lankford , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo prohibit National Laboratories from admitting certain foreign nationals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarding American Technology from Exploitation Act of 2025 or the GATE Act of 2025 .\n#### 2. Prohibition on National Laboratories admitting certain foreign nationals\n##### (a) Definitions\nIn this section:\n**(1) Assignee**\nThe term assignee means an individual who is seeking approval from, or has been approved by, a National Laboratory to access the premises, information, or technology of the National Laboratory for a period of more than 30 consecutive days.\n**(2) Covered foreign national**\n**(A) In general**\nThe term covered foreign national means a foreign national of any of the following countries:\n**(i)**\nThe People\u2019s Republic of China.\n**(ii)**\nThe Russian Federation.\n**(iii)**\nThe Islamic Republic of Iran.\n**(iv)**\nThe Democratic People\u2019s Republic of Korea.\n**(v)**\nThe Republic of Cuba.\n**(B) Exclusion**\nThe term covered foreign national does not include an individual that is\u2014\n**(i)**\nlawfully admitted for permanent residence (as defined in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) )); or\n**(ii)**\na citizen of the United States.\n**(3) Foreign national**\nThe term foreign national has the meaning given the term alien in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ).\n**(4) National Laboratory**\nThe term National Laboratory has the meaning given the term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).\n**(5) Senior counterintelligence official**\nThe term senior counterintelligence official means\u2014\n**(A)**\nthe Director of the Federal Bureau of Investigation;\n**(B)**\nthe Deputy Director of the Federal Bureau of Investigation;\n**(C)**\nthe Executive Assistant Director of the National Security Branch of the Federal Bureau of Investigation; and\n**(D)**\nthe Assistant Director of the Counterintelligence Division of the Federal Bureau of Investigation.\n**(6) Visitor**\nThe term visitor means an individual who is seeking approval from, or has been approved by, a National Laboratory to access the premises, information, or technology of the National Laboratory for any period shorter than a period described in paragraph (1).\n##### (b) Prohibition\n**(1) In general**\nExcept as provided in paragraph (2), beginning on the date of enactment of this Act, a National Laboratory\u2014\n**(A)**\nshall not admit as a visitor or assignee any covered foreign national; and\n**(B)**\nshall prohibit access to any visitor or assignee that is a covered foreign national and has sought or obtained approval to access the premises, information, or technology of the National Laboratory as of that date.\n**(2) Waiver**\nParagraph (1) shall not apply to a National Laboratory with respect to a covered foreign national if the Secretary of Energy, in consultation with the Director of the Office of Intelligence and Counterintelligence of the Department of Energy and a senior counterintelligence official\u2014\n**(A)**\ncertifies that the benefits to the United States of admittance or access to the National Laboratory by the covered foreign national outweigh the national security and economic risks to the United States; and\n**(B)**\nissues to the National Laboratory, in writing, a waiver of paragraph (1) with respect to the covered foreign national.\n**(3) Notification to Congress**\nNot later than 30 days after the date on which a waiver is issued under paragraph (2), the Secretary of Energy shall submit to the Select Committee on Intelligence of the Senate, the Committee on Energy and Natural Resources of the Senate, the Committee on Commerce, Science, and Transportation of the Senate, the Permanent Select Committee on Intelligence of the House of Representatives, the Committee on Energy and Commerce of the House of Representatives, and the Committee on Science, Space, and Technology of the House of Representatives a notification describing the waiver, including\u2014\n**(A)**\nthe country of origin of the covered foreign national who is the subject of the waiver;\n**(B)**\nthe date of the request by the covered foreign national for admission or access to the National Laboratory;\n**(C)**\nthe date on which the decision to issue the waiver was made; and\n**(D)**\nthe specific reasons for issuing the waiver.",
      "versionDate": "2025-03-11",
      "versionType": "Introduced in Senate"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-20T18:18:07Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s929is.xml"
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
      "title": "GATE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GATE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guarding American Technology from Exploitation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit National Laboratories from admitting certain foreign nationals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:06Z"
    }
  ]
}
```

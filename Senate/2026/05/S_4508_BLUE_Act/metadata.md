# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4508?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4508
- Title: BLUE Act
- Congress: 119
- Bill type: S
- Bill number: 4508
- Origin chamber: Senate
- Introduced date: 2026-05-13
- Update date: 2026-05-20T03:08:30Z
- Update date including text: 2026-05-20T03:08:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-13: Introduced in Senate
- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-13: Introduced in Senate

## Actions

- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4508",
    "number": "4508",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "BLUE Act",
    "type": "S",
    "updateDate": "2026-05-20T03:08:30Z",
    "updateDateIncludingText": "2026-05-20T03:08:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T14:57:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "AL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "TN"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "SD"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "UT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4508is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4508\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2026 Mr. Scott of Florida (for himself, Mr. Tuberville , Mrs. Blackburn , Mr. Rounds , Mr. Lee , Mr. Budd , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit the sharing of certain information about Federal law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Blocking Leaks Undermining Enforcement Act or the BLUE Act .\n#### 2. Prohibition on sharing of certain information\nSection 119 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking or at the end;\n**(B)**\nin paragraph (2), by striking the comma at the end and inserting ; or ; and\n**(C)**\nby inserting after paragraph (2) the following:\n(3) in the case of a covered person who is a Federal law enforcement officer, with the intent to physically obstruct, impede, interfere with, or retaliate against, or to aid another in physically obstructing, impeding, interfering with, or retaliating against, any lawful duty, investigation, operation, or official proceeding of the United States involving such officer, ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting , and, with respect to a Federal law enforcement officer, any physical location at which such officer is or is reasonably expected to be present (whether on or off duty) after that individual ; and\n**(B)**\nby amending paragraph (4) to read as follows:\n(4) the terms Federal law enforcement officer and immediate family have the meanings given the terms in section 115. .",
      "versionDate": "2026-05-13",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4508is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BLUE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T03:08:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Blocking Leaks Undermining Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T03:08:30Z"
    },
    {
      "title": "BLUE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T03:08:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the sharing of certain information about Federal law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T03:03:25Z"
    }
  ]
}
```

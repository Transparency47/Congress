# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1856?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1856
- Title: CASE LOAD Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1856
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-04-13T15:04:16Z
- Update date including text: 2026-04-13T15:04:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1856",
    "number": "1856",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CASE LOAD Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-13T15:04:16Z",
    "updateDateIncludingText": "2026-04-13T15:04:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:02:00Z",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1856ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1856\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Costa (for himself and Mr. Obernolte ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize additional district judges for the district court for the eastern district of California.\n#### 1. Short title\nThis Act may be cited as the Creating Additional Seats to Ease Legally Overburdened Adjudicators\u2019 Dockets Act of 2025 or the CASE LOAD Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Federal district court for the eastern district of California is the Federal trial court for 34 counties, including five of the fastest-growing cities in the State of California, serving a population of approximately 8,400,000.\n**(2)**\nThe Federal district court for the eastern district of California is one of the largest judicial districts in the country, with approximately 8,400,000 residents and over 87,000 square miles of land. Yet, there are only six permanent judgeships, with one upcoming vacancy pending a nomination elevating a sitting district judge.\n**(3)**\nBased on the 2019 U.S. census data, the ratio of authorized district judgeships to population was 1:1,362,552. The central district of California has the next highest ratio in the State, nearly half the size, with 1:694,323.\n**(4)**\nAs of June 2022, the total pending cases per judgeship in the Federal district court for the eastern district of California was 1,308, over 2.6 times larger than the average for all districts within the United States Court of Appeals for the Ninth Circuit. Pending caseloads remain high, and if a new vacancy opens upon the elevation of the district judge, caseloads will once again reach this unsustainable level.\n#### 3. Additional district judges for the eastern district of California\n##### (a) 2027\n**(1) Additional judgeships**\nOn or after January 21, 2027, the President shall appoint, by and with the advice and consent of the Senate, 2 additional district judges for the eastern district of California.\n**(2) Clerical amendment**\nThe table contained in section 133(a) of title 28, United States Code, is amended by striking the items relating to California and inserting the following:\nCalifornia: Northern 14 Eastern 8 Central 27 Southern 13 .\n**(3) Effective date**\nThe amendment made by paragraph (2) shall take effect on January 20, 2027.\n##### (b) 2029\n**(1) Additional judgeships**\nOn or after January 5, 2029, the President shall appoint, by and with the advice and consent of the Senate, 1 additional district judge for the eastern district of California.\n**(2) Clerical amendment**\nThe table contained in section 133(a) of title 28, United States Code, is amended by striking the items relating to California and inserting the following:\nCalifornia: Northern 14 Eastern 9 Central 27 Southern 13 .\n**(3) Effective date**\nThe amendment made by paragraph (2) shall take effect on January 4, 2029.\n##### (c) 2031\n**(1) Additional judgeships**\nOn or after January 21, 2031, the President shall appoint, by and with the advice and consent of the Senate, 2 additional district judges for the eastern district of California.\n**(2) Clerical amendment**\nThe table contained in section 133(a) of title 28, United States Code, is amended by striking the items relating to California and inserting the following:\nCalifornia: Northern 14 Eastern 11 Central 27 Southern 13 .\n**(3) Effective date**\nThe amendment made by paragraph (2) shall take effect on January 20, 2031.\n#### 4. Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this Act and the amendments made by this Act, including such sums as may be necessary to provide appropriate space and facilities for the judicial positions created by this Act or an amendment made by this Act.",
      "versionDate": "2025-03-05",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "California",
            "updateDate": "2026-04-13T15:04:02Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2026-04-13T15:04:10Z"
          },
          {
            "name": "Judges",
            "updateDate": "2026-04-13T15:04:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-03-21T18:41:40Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1856ih.xml"
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
      "title": "CASE LOAD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CASE LOAD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Creating Additional Seats to Ease Legally Overburdened Adjudicators\u2019 Dockets Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize additional district judges for the district court for the eastern district of California.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:05Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/371?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/371
- Title: SBA Disaster Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 371
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2025-12-18T12:03:18Z
- Update date including text: 2025-12-18T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-12 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported without amendment favorably.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.
- 2025-03-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 23.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-12 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported without amendment favorably.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.
- 2025-03-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 23.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/371",
    "number": "371",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "SBA Disaster Transparency Act",
    "type": "S",
    "updateDate": "2025-12-18T12:03:18Z",
    "updateDateIncludingText": "2025-12-18T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 23.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-03",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-03",
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
        "item": [
          {
            "date": "2025-03-04T22:11:41Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-12T14:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-03T22:45:08Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "TN"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s371is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 371\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mr. Scott of South Carolina (for himself, Mr. Schiff , Mr. Budd , Mrs. Blackburn , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo require certain reports on small business disaster assistance to be published on the website of the Small Business Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SBA Disaster Transparency Act .\n#### 2. Publication of reports on disaster assistance\nSection 12091 of the Small Business Disaster Response and Loan Improvements Act of 2008 ( 15 U.S.C. 636k ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by inserting and publish on the website of the Administration after Representatives ; and\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting and published after submitted ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting and publish on the website of the Administration after Representatives ; and\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting and published after submitted ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by inserting and publish on the website of the Administration after Representatives ; and\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting and published after submitted ; and\n**(4)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking a report ; and\n**(ii)**\nby inserting and publish on the website of the Administration a report after Representatives ; and\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting and published after submitted .",
      "versionDate": "2025-02-03",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s371rs.xml",
      "text": "II\nCalendar No. 23\n119th CONGRESS\n1st Session\nS. 371\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mr. Scott of South Carolina (for himself, Mr. Schiff , Mr. Budd , Mrs. Blackburn , Mr. Scott of Florida , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nMarch 4, 2025 Reported by Ms. Ernst , without amendment\nA BILL\nTo require certain reports on small business disaster assistance to be published on the website of the Small Business Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SBA Disaster Transparency Act .\n#### 2. Publication of reports on disaster assistance\nSection 12091 of the Small Business Disaster Response and Loan Improvements Act of 2008 ( 15 U.S.C. 636k ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by inserting and publish on the website of the Administration after Representatives ; and\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting and published after submitted ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting and publish on the website of the Administration after Representatives ; and\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting and published after submitted ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by inserting and publish on the website of the Administration after Representatives ; and\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting and published after submitted ; and\n**(4)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking a report ; and\n**(ii)**\nby inserting and publish on the website of the Administration a report after Representatives ; and\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting and published after submitted .",
      "versionDate": "2025-03-04",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-02-21",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "1475",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SBA Disaster Transparency Act",
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
            "name": "Disaster relief and insurance",
            "updateDate": "2025-02-20T18:57:06Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-20T19:01:12Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-02-20T19:01:05Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-02-20T18:57:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-07T13:09:30Z"
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
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s371is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s371rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SBA Disaster Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:18Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "SBA Disaster Transparency Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-03-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SBA Disaster Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T13:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require certain reports on small business disaster assistance to be published on the website of the Small Business Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T13:18:19Z"
    }
  ]
}
```

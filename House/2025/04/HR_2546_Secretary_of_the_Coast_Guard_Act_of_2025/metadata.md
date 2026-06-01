# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2546?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2546
- Title: Secretary of the Coast Guard Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2546
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2025-06-12T08:06:20Z
- Update date including text: 2025-06-12T08:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-01 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-01 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2546",
    "number": "2546",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "E000235",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Ezell, Mike [R-MS-4]",
        "lastName": "Ezell",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Secretary of the Coast Guard Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-12T08:06:20Z",
    "updateDateIncludingText": "2025-06-12T08:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:08:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-01T20:51:56Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "FL"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AK"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "FL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2546ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2546\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Ezell introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish the position of Secretary of the Coast Guard, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secretary of the Coast Guard Act of 2025 .\n#### 2. Secretary of the Coast Guard\n##### (a) Secretary of the Coast Guard\nSubtitle I of title 14, United States Code, is amended\u2014\n**(1)**\nby redesignating section 106 as section 107;\n**(2)**\nby inserting after section 105 the following:\n106. Secretary of the Coast Guard defined In this title, the term Secretary of the Coast Guard means the Secretary of the Coast Guard established in section 201. ; and\n**(3)**\nby inserting after section 107, as so redesignated, the following:\n2 Secretary of the Coast Guard 201. Secretary of the Coast Guard. 201. Secretary of the Coast Guard (a) In general There is a Secretary of the Coast Guard, appointed by the President, by and with the advice and consent of the Senate. (b) Powers Subject to the authority, direction, and control of the Secretary, the Secretary of the Coast Guard shall exercise the powers of the Secretary in section 501, and other duties as may be prescribed by law or by the President or Secretary, in directing the Coast Guard. (c) Reporting The Secretary of the Coast Guard shall report directly to the Secretary without being required to report through any other official of the department in which the Coast Guard is operating. (d) Commandant reporting The Commandment shall report directly to the Secretary of the Coast Guard. .\n##### (b) Clerical amendment\nThe analysis for chapter 1 of title 14, United States Code, is amended by striking the item relating to section 106 and inserting the following:\n106. Secretary of the Coast Guard defined. 107. Commandant defined. .",
      "versionDate": "2025-04-01",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-28T14:17:49Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2546ih.xml"
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
      "title": "Secretary of the Coast Guard Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T06:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secretary of the Coast Guard Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T06:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the position of Secretary of the Coast Guard, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T06:33:31Z"
    }
  ]
}
```

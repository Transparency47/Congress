# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/499?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/499
- Title: To rename the medical center of the Department of Veterans Affairs in Dallas, Texas, as the "Eddie Bernice Johnson VA Medical Center".
- Congress: 119
- Bill type: HR
- Bill number: 499
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-12-20T09:06:45Z
- Update date including text: 2025-12-20T09:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/499",
    "number": "499",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001130",
        "district": "30",
        "firstName": "Jasmine",
        "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
        "lastName": "Crockett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "To rename the medical center of the Department of Veterans Affairs in Dallas, Texas, as the \"Eddie Bernice Johnson VA Medical Center\".",
    "type": "HR",
    "updateDate": "2025-12-20T09:06:45Z",
    "updateDateIncludingText": "2025-12-20T09:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:08:07Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr499ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 499\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Ms. Crockett (for herself, Mr. Gooden , Ms. Garcia of Texas , Mr. Castro of Texas , Mr. Cuellar , Mr. Green of Texas , and Ms. Escobar ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo rename the medical center of the Department of Veterans Affairs in Dallas, Texas, as the Eddie Bernice Johnson VA Medical Center .\n#### 1. Findings\nCongress finds the following:\n**(1)**\nCongresswoman Eddie Bernice Johnson served the veteran community diligently during her 16 years working as the Chief Psychiatric Nurse of the medical center of the Department of Veterans Affairs in Dallas, Texas.\n**(2)**\nThroughout her 30 years in Congress, Congresswoman Eddie Bernice Johnson introduced numerous bills that sought to honor and serve the patriots who so nobly served their country.\n**(3)**\nCongresswoman Eddie Bernice Johnson introduced, and won passage of, the Dr. James Allen Veteran Vision Equity Act of 2007 ( Public Law 110\u2013157 ; 38 U.S.C. 101 note), which assists those wounded in service in the Armed Forces in receiving the treatment they need, and increases the dignity shown to those who gave their last full measure of devotion to the country that they served.\n**(4)**\nCongresswoman Eddie Bernice Johnson was a trailblazer who worked tirelessly on behalf of veterans in the United States and has earned the respect and honor of her native city of Dallas, Texas, the State of Texas, the United States, and Congress.\n#### 2. Designation of Eddie Bernice Johnson VA Medical Center\n##### (a) Designation\nThe medical center of the Department of Veterans Affairs located at 4500 South Lancaster Road, Dallas, Texas, shall after the date of the enactment of this Act be known and designated as the Eddie Bernice Johnson Department of Veterans Affairs Medical Center or the Eddie Bernice Johnson VA Medical Center .\n##### (b) Reference\nAny reference in any law, regulation, map, document, paper, or other record of the United States to the medical center referred to in subsection (a) shall be considered to be a reference to the Eddie Bernice Johnson VA Medical Center.",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "116",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to rename the medical center of the Department of Veterans Affairs in Dallas, Texas, as the \"Eddie Bernice Johnson VA Medical Center\".",
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
            "name": "Congressional tributes",
            "updateDate": "2025-03-20T13:59:26Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-03-20T13:59:22Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-03-20T13:59:17Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-03-20T13:59:31Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-20T13:59:12Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-03-20T13:59:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-18T17:37:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr499",
          "measure-number": "499",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr499v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill designates the medical center of the Department of Veterans Affairs in Dallas, Texas, as the Eddie Bernice Johnson Department of Veterans Affairs Medical Center or the Eddie Bernice Johnson VA Medical Center.</p>"
        },
        "title": "To rename the medical center of the Department of Veterans Affairs in Dallas, Texas, as the \"Eddie Bernice Johnson VA Medical Center\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr499.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates the medical center of the Department of Veterans Affairs in Dallas, Texas, as the Eddie Bernice Johnson Department of Veterans Affairs Medical Center or the Eddie Bernice Johnson VA Medical Center.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr499"
    },
    "title": "To rename the medical center of the Department of Veterans Affairs in Dallas, Texas, as the \"Eddie Bernice Johnson VA Medical Center\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates the medical center of the Department of Veterans Affairs in Dallas, Texas, as the Eddie Bernice Johnson Department of Veterans Affairs Medical Center or the Eddie Bernice Johnson VA Medical Center.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr499"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr499ih.xml"
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
      "title": "To rename the medical center of the Department of Veterans Affairs in Dallas, Texas, as the \"Eddie Bernice Johnson VA Medical Center\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:33:38Z"
    },
    {
      "title": "To rename the medical center of the Department of Veterans Affairs in Dallas, Texas, as the \"Eddie Bernice Johnson VA Medical Center\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-17T09:05:42Z"
    }
  ]
}
```

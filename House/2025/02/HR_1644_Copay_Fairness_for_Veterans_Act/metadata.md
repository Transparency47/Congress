# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1644?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1644
- Title: Copay Fairness for Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 1644
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-09-19T08:07:35Z
- Update date including text: 2025-09-19T08:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Health.
- 2025-03-25 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-03-25 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Health.
- 2025-03-25 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-03-25 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1644",
    "number": "1644",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Copay Fairness for Veterans Act",
    "type": "HR",
    "updateDate": "2025-09-19T08:07:35Z",
    "updateDateIncludingText": "2025-09-19T08:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
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
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-03-25T21:39:25Z",
                "name": "Reported by"
              },
              {
                "date": "2025-03-25T18:12:55Z",
                "name": "Reported by"
              },
              {
                "date": "2025-03-25T18:12:45Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-10T21:33:24Z",
                "name": "Referred to"
              }
            ]
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CT"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "DC"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1644ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1644\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Underwood (for herself, Mr. Moulton , Mrs. Hayes , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to eliminate copayments by the Department of Veterans Affairs for medicines relating to preventive health services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Copay Fairness for Veterans Act .\n#### 2. Improvement to preventive health services furnished by Department of Veterans Affairs\n##### (a) Elimination of medication copayments\nSection 1722A(a)(3) of title 38, United States Code, is amended\u2014\n**(1)**\nin subparagraph (C), by striking or ;\n**(2)**\nin subparagraph (D), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(E) to medication that is or is part of a preventive health service. .\n##### (b) Elimination of hospital care and medical services copayments\nSection 1710 of such title is amended\u2014\n**(1)**\nin subsection (f)\u2014\n**(A)**\nby redesignating paragraph (5) as paragraph (6); and\n**(B)**\nby inserting after paragraph (4) the following new paragraph (5):\n(5) A veteran shall not be liable to the United States under this subsection for any amounts for preventive health services. ; and\n**(2)**\nin subsection (g)(3), by adding at the end the following new subparagraph:\n(C) Preventive health services. .\n##### (c) Definition\nSection 1701(9) of such title is amended\u2014\n**(1)**\nin subparagraph (K), by striking ; and and inserting a semicolon;\n**(2)**\nby redesignating subparagraph (L) as subparagraph (O); and\n**(3)**\nby inserting after subparagraph (K) the following new subparagraphs:\n(L) evidence-based items or services that have in effect a rating of A or B in the current recommendations of the United States Preventive Services Task Force; (M) immunizations that have in effect a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the individual involved; (N) with respect to services for women\u2014 (i) the preventive care, screenings, and contraceptives provided for in the Health Resources and Services Administration Preventive Services Guidelines in effect as of December 30, 2022; and (ii) any contraceptive approved, granted, or cleared by the Food and Drug Administration, any related contraceptive care, and any related services; and .",
      "versionDate": "2025-02-27",
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
            "name": "Family planning and birth control",
            "updateDate": "2025-04-01T15:27:19Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-04-01T15:27:03Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-04-01T15:26:58Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-04-01T15:27:34Z"
          },
          {
            "name": "Immunology and vaccination",
            "updateDate": "2025-04-01T15:27:29Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-01T15:27:08Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-04-01T15:26:51Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-04-01T15:27:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-25T17:59:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1644",
          "measure-number": "1644",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1644v00",
            "update-date": "2025-04-09"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Copay Fairness for Veterans Act</strong></p><p>This bill eliminates veterans' copayments for medication, hospital care, and medical services related to preventive health services provided by the Department of Veterans Affairs.</p><p>The bill expands the definition of preventive health services to include (1) evidence-based items or services that have an A or B rating in the recommendations of the United States Preventive Services Task Force; (2) immunizations that have a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the individual involved; and (3) with respect to services for women, the preventive care, screenings, and contraceptives provided for in the Health Resources and Services Administration Preventive Services Guidelines in effect as of December 30, 2022, and any contraceptive approved, granted, or cleared by the Food and Drug Administration, any related contraceptive care, and any related services.</p>"
        },
        "title": "Copay Fairness for Veterans Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1644.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Copay Fairness for Veterans Act</strong></p><p>This bill eliminates veterans' copayments for medication, hospital care, and medical services related to preventive health services provided by the Department of Veterans Affairs.</p><p>The bill expands the definition of preventive health services to include (1) evidence-based items or services that have an A or B rating in the recommendations of the United States Preventive Services Task Force; (2) immunizations that have a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the individual involved; and (3) with respect to services for women, the preventive care, screenings, and contraceptives provided for in the Health Resources and Services Administration Preventive Services Guidelines in effect as of December 30, 2022, and any contraceptive approved, granted, or cleared by the Food and Drug Administration, any related contraceptive care, and any related services.</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119hr1644"
    },
    "title": "Copay Fairness for Veterans Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Copay Fairness for Veterans Act</strong></p><p>This bill eliminates veterans' copayments for medication, hospital care, and medical services related to preventive health services provided by the Department of Veterans Affairs.</p><p>The bill expands the definition of preventive health services to include (1) evidence-based items or services that have an A or B rating in the recommendations of the United States Preventive Services Task Force; (2) immunizations that have a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the individual involved; and (3) with respect to services for women, the preventive care, screenings, and contraceptives provided for in the Health Resources and Services Administration Preventive Services Guidelines in effect as of December 30, 2022, and any contraceptive approved, granted, or cleared by the Food and Drug Administration, any related contraceptive care, and any related services.</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119hr1644"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1644ih.xml"
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
      "title": "Copay Fairness for Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Copay Fairness for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to eliminate copayments by the Department of Veterans Affairs for medicines relating to preventive health services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:33Z"
    }
  ]
}
```

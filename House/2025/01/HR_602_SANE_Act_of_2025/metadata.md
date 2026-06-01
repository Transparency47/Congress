# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/602?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/602
- Title: SANE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 602
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2026-02-03T09:05:52Z
- Update date including text: 2026-02-03T09:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/602",
    "number": "602",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "SANE Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:52Z",
    "updateDateIncludingText": "2026-02-03T09:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-04T22:40:29Z",
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
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "SC"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NV"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr602ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 602\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Burchett (for himself, Mr. Kennedy of New York , Mrs. Luna , Mr. Moskowitz , Ms. Mace , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to ensure that sexual assault nurse examiners are employed at certain Department of Veterans Affairs medical facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sexual Assault Nurse Examiner in VA Hospitals Act of 2025 or the SANE Act of 2025 .\n#### 2. Qualifications of health care providers who perform sexual assault examinations at certain Department of Veterans Affairs medical facilities\n##### (a) In general\nThe Secretary of Veterans Affairs shall employ, at each hospital and urgent care facility of the Department of Veterans Affairs\u2014\n**(1)**\nat least one sexual assault nurse examiner; or\n**(2)**\nif the Secretary cannot so employ a sexual assault nurse examiner, a health care provider qualified to conduct a sexual assault forensic examination.\n##### (b) Mental health care referral\nAfter examining an individual for sexual assault, a health care provider of the Department shall verbally refer the individual to mental health care services furnished by the Secretary\u2014\n**(1)**\nin a hospital of the Department; or\n**(2)**\npursuant to a Veterans Care Agreement under section 1703A of title 38, United States Code, if the wait time for services described in paragraph (1) exceeds 30 days.\n##### (c) Dedicated responsibilities\nIn carrying out this section, the Secretary shall ensure that there is no reduction in, or negative effect on, the patient care responsibilities that are otherwise carried out by employees of the Department.\n##### (d) Definitions\nIn this section, the terms sexual assault nurse examiner and sexual assault forensic examination have the meanings given such terms in section 304(a) of the DNA Sexual Assault Justice Act of 2004 ( 34 U.S.C. 40723(a) ).",
      "versionDate": "2025-01-22",
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
            "name": "Assault and harassment offenses",
            "updateDate": "2025-03-13T15:39:27Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-13T15:39:35Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-13T15:39:21Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-03-13T15:39:40Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-03-13T15:39:31Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-13T15:39:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-25T14:44:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr602",
          "measure-number": "602",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr602v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sexual Assault Nurse Examiner in VA Hospitals Act of 2025 or the SANE Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to employ at each of its hospitals and urgent care facilities at least one sexual assault nurse examiner or a health care provider who is qualified to conduct a sexual assault forensic examination.</p><p>The bill also provides that after examining an individual for sexual assault, a VA health care provider must verbally refer the individual to mental health care services furnished by the VA in a VA hospital or by a non-VA provider under the Veterans Community Care Program if the wait time for services at a VA hospital exceeds 30 days.</p><p>In providing such duties related to sexual assault care, the VA must ensure that there is no reduction in, or negative effect on, the patient care responsibilities otherwise carried out by its employees.</p>"
        },
        "title": "SANE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr602.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sexual Assault Nurse Examiner in VA Hospitals Act of 2025 or the SANE Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to employ at each of its hospitals and urgent care facilities at least one sexual assault nurse examiner or a health care provider who is qualified to conduct a sexual assault forensic examination.</p><p>The bill also provides that after examining an individual for sexual assault, a VA health care provider must verbally refer the individual to mental health care services furnished by the VA in a VA hospital or by a non-VA provider under the Veterans Community Care Program if the wait time for services at a VA hospital exceeds 30 days.</p><p>In providing such duties related to sexual assault care, the VA must ensure that there is no reduction in, or negative effect on, the patient care responsibilities otherwise carried out by its employees.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr602"
    },
    "title": "SANE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sexual Assault Nurse Examiner in VA Hospitals Act of 2025 or the SANE Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to employ at each of its hospitals and urgent care facilities at least one sexual assault nurse examiner or a health care provider who is qualified to conduct a sexual assault forensic examination.</p><p>The bill also provides that after examining an individual for sexual assault, a VA health care provider must verbally refer the individual to mental health care services furnished by the VA in a VA hospital or by a non-VA provider under the Veterans Community Care Program if the wait time for services at a VA hospital exceeds 30 days.</p><p>In providing such duties related to sexual assault care, the VA must ensure that there is no reduction in, or negative effect on, the patient care responsibilities otherwise carried out by its employees.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr602"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr602ih.xml"
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
      "title": "SANE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SANE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sexual Assault Nurse Examiner in VA Hospitals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to ensure that sexual assault nurse examiners are employed at certain Department of Veterans Affairs medical facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T06:49:32Z"
    }
  ]
}
```

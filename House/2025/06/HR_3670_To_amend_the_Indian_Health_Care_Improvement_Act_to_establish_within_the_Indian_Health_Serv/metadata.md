# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3670?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3670
- Title: IHS Provider Expansion Act
- Congress: 119
- Bill type: HR
- Bill number: 3670
- Origin chamber: House
- Introduced date: 2025-06-02
- Update date: 2026-04-22T08:07:33Z
- Update date including text: 2026-04-22T08:07:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-02: Introduced in House
- 2025-06-02 - IntroReferral: Introduced in House
- 2025-06-02 - IntroReferral: Introduced in House
- 2025-06-02 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-02 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-06-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H2428)
- 2025-06-11 - Committee: Subcommittee Hearings Held
- Latest action: 2025-06-02: Introduced in House

## Actions

- 2025-06-02 - IntroReferral: Introduced in House
- 2025-06-02 - IntroReferral: Introduced in House
- 2025-06-02 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-02 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-06-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H2428)
- 2025-06-11 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-02",
    "latestAction": {
      "actionDate": "2025-06-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3670",
    "number": "3670",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "S001218",
        "district": "1",
        "firstName": "Melanie",
        "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
        "lastName": "Stansbury",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "IHS Provider Expansion Act",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:33Z",
    "updateDateIncludingText": "2026-04-22T08:07:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2428)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-02",
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
          "date": "2025-06-02T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-11T17:41:20Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-04T14:14:04Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-02T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "NM"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3670ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3670\nIN THE HOUSE OF REPRESENTATIVES\nJune 2, 2025 Ms. Stansbury (for herself and Ms. Leger Fernandez ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Indian Health Care Improvement Act to establish within the Indian Health Service an Office of Graduate Medical Education Programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the IHS Provider Expansion Act .\n#### 2. Indian Health Service Office of Graduate Medical Education Programs\nTitle I of the Indian Health Care Improvement Act ( 25 U.S.C. 1611 et seq. ) is amended by adding at the end the following:\n125. Office of Graduate Medical Education Programs (a) Establishment The Secretary, acting through the Service, (in this section referred to as the Secretary ) shall establish within the Service an Office of Graduate Medical Education Programs (in this section referred to as the Office ). (b) Duties The Office shall have the following duties: (1) To create a pipeline for future health care professionals, paraprofessionals, and other health-related professionals (as identified by the Secretary) to participate in residency and fellowship programs. (2) To oversee current residency and fellowship programs at facilities of the Service and facilitate the establishment of additional residency programs that support recruitment and retention of health care professionals, paraprofessionals, and other health-related professionals (as identified by the Secretary) working at such facilities. (3) To serve as the central hub for residency programs at facilities of the Service. (4) To work in consultation or coordination with academic institutions. (5) To coordinate medical student and elective rotational and education track programs. (c) Interagency working group (1) In general The Secretary, in consultation with the Secretary of Veterans Affairs, the Secretary of Labor, the Administrator of the Health Resources and Services Administration, and the Administrator of the Centers for Medicare & Medicaid Services, shall establish an interagency working group (in this subsection referred to as the working group ) to assist the Secretary in establishing the Office under subsection (a), including by\u2014 (A) supporting the implementation of the Office; and (B) developing long-term planning for long-term sustainability of the Office. (2) Quarterly reports Not later than the date that is 120 days after the date of enactment of this section, and every 3 months thereafter, the working group shall submit to Congress a report on the activities of the working group. (3) Termination The working group shall terminate on the date that is 10 years after the date of enactment of this section. (d) Authorization of appropriations Subject to the availability of appropriations, there is authorized to be appropriated to carry out this section, not less than\u2014 (1) $4,000,000 for fiscal year 2027; and (2) $4,000,000 for each subsequent fiscal year. .",
      "versionDate": "2025-06-02",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-11T18:33:18Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-07-11T18:32:52Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-07-11T18:33:04Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-07-11T18:32:57Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-07-11T18:33:11Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2025-07-11T18:32:40Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-07-11T18:32:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-07-01T16:35:27Z"
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
      "date": "2025-06-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3670ih.xml"
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
      "title": "IHS Provider Expansion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "IHS Provider Expansion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Indian Health Care Improvement Act to establish within the Indian Health Service an Office of Graduate Medical Education Programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:24Z"
    }
  ]
}
```

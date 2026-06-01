# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4063?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4063
- Title: Veterans Full-Service Care and Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4063
- Origin chamber: House
- Introduced date: 2025-06-20
- Update date: 2025-12-20T09:06:56Z
- Update date including text: 2025-12-20T09:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-20: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-06-20: Introduced in House

## Actions

- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-20",
    "latestAction": {
      "actionDate": "2025-06-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4063",
    "number": "4063",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Veterans Full-Service Care and Access Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-20T09:06:56Z",
    "updateDateIncludingText": "2025-12-20T09:06:56Z"
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
      "actionDate": "2025-06-20",
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
      "actionDate": "2025-06-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-20",
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
          "date": "2025-06-20T15:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:03:02Z",
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
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4063ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4063\nIN THE HOUSE OF REPRESENTATIVES\nJune 20, 2025 Mr. Pappas (for himself and Ms. Goodlander ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to ensure that veterans in each of the 48 contiguous States are able to receive services in at least one full-service hospital of the Veterans Health Administration in the State or receive comparable services provided by contract in the State.\n#### 1. Short title\nThis Act may be cited as the Veterans Full-Service Care and Access Act of 2025 .\n#### 2. Availability of full-service hospital of the Veterans Health Administration in certain States or provision of comparable services through contract with other health care providers in the State\n##### (a) In general\nChapter 17 of title 38, United States Code, is amended by inserting after section 1716 the following new section:\n1716A. Access to full-service hospitals in certain States or comparable services through contract (a) Requirement With respect to each of the 48 contiguous States, the Secretary shall ensure that veterans in the State eligible for hospital care and medical services under section 1710 of this title shall receive such hospital care and medical services at not fewer than one full-service hospital of the Veterans Health Administration located within the geographic boundaries of the State. (b) Rule of construction Nothing in subsection (a) shall be construed to restrict the ability of the Secretary to provide enhanced care to an eligible veteran who resides in one State in a hospital of the Veterans Health Administration in another State. .\n##### (b) Conforming amendments to Veterans Community Care Program\nSection 1703(d)(1) of such title is amended in subparagraph (B) by inserting as of the date of the enactment of the Veterans Full-Service Care and Access Act of 2025 before the semicolon at the end.\n##### (c) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1716 the following new item:\n1716A. Access to full-service hospitals in certain States or comparable services through contract. .\n##### (d) Report on implementation\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Congress a report describing the extent to which the Secretary has complied with the requirement imposed by section 1716A of title 38, United States Code, as added by subsection (a), including the effect of such requirement on improving the quality and standards of care provided to veterans.",
      "versionDate": "2025-06-20",
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
        "actionDate": "2025-06-18",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "2134",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans Full-Service Care and Access Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-09T15:27:43Z"
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
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4063ih.xml"
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
      "title": "Veterans Full-Service Care and Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T07:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Full-Service Care and Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to ensure that veterans in each of the 48 contiguous States are able to receive services in at least one full-service hospital of the Veterans Health Administration in the State or receive comparable services provided by contract in the State.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:18:57Z"
    }
  ]
}
```

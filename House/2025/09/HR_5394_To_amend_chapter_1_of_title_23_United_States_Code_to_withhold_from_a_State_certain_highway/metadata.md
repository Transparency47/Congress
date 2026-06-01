# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5394?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5394
- Title: Freedom from Automated Speed Enforcement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5394
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-10-07T08:05:28Z
- Update date including text: 2025-10-07T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-17 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-17 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5394",
    "number": "5394",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Freedom from Automated Speed Enforcement Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:28Z",
    "updateDateIncludingText": "2025-10-07T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-17T21:45:09Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "AL"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5394ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5394\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Harrigan (for himself, Mr. Crenshaw , Mr. Moore of Alabama , Mr. Perry , and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend chapter 1 of title 23, United States Code, to withhold from a State certain highway funds if the State operates an automated speed enforcement system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom from Automated Speed Enforcement Act of 2025 .\n#### 2. Automated speed enforcement system\n##### (a) In general\nChapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Automated speed enforcement system (a) Withholding of apportionments for noncompliance The Secretary shall withhold 10 percent of the amount required to be apportioned to any State under each of paragraphs (1) and (2) of section 104(b) on the first day of each fiscal year, beginning after September 30, 2026, in which the State fails to submit the certification described in subsection (b). (b) Annual certification (1) In general To be in compliance under subsection (a), the Governor of a State shall submit to the Secretary a certification that no jurisdiction in such State operates an automated speed enforcement system. (2) Audit To verify such certification, the Secretary may conduct an audit or require documentation as the Secretary determines necessary. (c) Exception for school and work zones Notwithstanding subsection (b), a State may operate an automated speed enforcement system in\u2014 (1) a designated school zone during posted school hours; and (2) an active construction work zone\u2014 (A) for the duration of the construction project; and (B) if\u2014 (i) when the location in which the automated speed system is operating is not an active construction work zone, the posted speed limit is less than 55 miles per hour; and (ii) such zone displays clear signage indicating that\u2014 (I) the area is a construction zone; and (II) there is an automated speed enforcement system in use. (d) Definition of automated speed enforcement system In this section, the term automated speed enforcement system means any device that\u2014 (1) captures an image of a vehicle for the purpose of issuing a citation for exceeding a speed limit; and (2) operates without the presence of a law enforcement officer. .\n##### (b) Regulations\nThe Secretary of Transportation may issue such regulations as are necessary to carry out section 180 of title 23, United States Code (as added by this Act).\n##### (c) Clerical amendment\nThe analysis for chapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Automated speed enforcement system. .",
      "versionDate": "2025-09-16",
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
        "updateDate": "2025-09-25T14:26:48Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5394ih.xml"
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
      "title": "Freedom from Automated Speed Enforcement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom from Automated Speed Enforcement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 1 of title 23, United States Code, to withhold from a State certain highway funds if the State operates an automated speed enforcement system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:29Z"
    }
  ]
}
```

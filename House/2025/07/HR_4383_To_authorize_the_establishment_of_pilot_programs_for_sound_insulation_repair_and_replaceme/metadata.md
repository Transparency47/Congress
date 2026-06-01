# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4383?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4383
- Title: Sound Insulation Treatment Repair and Replacement Program Act
- Congress: 119
- Bill type: HR
- Bill number: 4383
- Origin chamber: House
- Introduced date: 2025-07-14
- Update date: 2026-01-05T22:01:04Z
- Update date including text: 2026-01-05T22:01:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-14: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-15 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-07-14: Introduced in House

## Actions

- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-15 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4383",
    "number": "4383",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S000510",
        "district": "9",
        "firstName": "Adam",
        "fullName": "Rep. Smith, Adam [D-WA-9]",
        "lastName": "Smith",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Sound Insulation Treatment Repair and Replacement Program Act",
    "type": "HR",
    "updateDate": "2026-01-05T22:01:04Z",
    "updateDateIncludingText": "2026-01-05T22:01:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-14",
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
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T16:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-15T19:35:28Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4383ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4383\nIN THE HOUSE OF REPRESENTATIVES\nJuly 14, 2025 Mr. Smith of Washington introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo authorize the establishment of pilot programs for sound insulation repair and replacement.\n#### 1. Short title\nThis Act may be cited as the Sound Insulation Treatment Repair and Replacement Program Act .\n#### 2. Pilot program for sound insulation repair and replacement\n##### (a) Government share\nSection 47109 of title 49, United States Code, is amended by adding at the end the following:\n(i) Special rule for sound insulation repair and replacement With respect to a project to carry out sound insulation that is granted a waiver under section 47110(j), the allowable project cost for such project shall be calculated without consideration of any costs that were previously paid by the Government. .\n##### (b) Sound insulation treatment repair and replacement projects\nSection 47110 of title 49, United States Code, is amended by adding at the end the following:\n(j) Pilot program for sound insulation repair and replacements (1) In general Not later than 120 days after the date of enactment of this subsection, the Administrator of the Federal Aviation Administration shall establish a pilot program at up to 4 large hub public-use airports for local airport operators that have established a local program to fund secondary noise using non-aeronautical revenue that provides a one-time waiver of the requirement of subsection (b)(4) for a qualifying airport as applied to projects to carry out repair and replacement of sound insulation for a residential building for which the airport previously received Federal assistance or Federally authorized airport assistance under this subchapter if\u2014 (A) the Secretary determines that the additional assistance is justified due to the residence containing any sound insulation treatment or other type of sound proofing material previously installed under this subchapter that is determined to be eligible pursuant to paragraph (2); and (B) the residence\u2014 (i) falls within the Day Night Level (DNL) of 65 to 75 decibel (dB) noise contours, according to the most recent noise exposure map (as such term is defined in section 150.7 of title 14, Code of Federal Regulations) available as of the date of enactment of this subsection; (ii) fell within such noise contours at the time the initial sound insulation treatment was installed, but a qualified noise auditor has determined that\u2014 (I) such sound insulation treatment caused physical damage to the residence; or (II) the materials used for sound insulation treatment were of low quality and have deteriorated, broken, or otherwise no longer function as intended; and (iii) is shown through testing that current interior noise levels exceed DNL 45 dB, and the new insulation would have the ability to achieve a 5 dB noise reduction; (2) Eligibility determination To be eligible for waiver under this subsection for repair or replacement of sound insulation treatment projects, an applicant shall\u2014 (A) ensure that the applicant and the property owner have made a good faith effort to exhaust any amounts available through warranties, insurance coverage, and legal remedies for the sound insulation treatment previously installed on the eligible residence; (B) verify the sound insulation treatment for which Federal assistance was previously provided was installed prior to the year 2002; and (C) demonstrate that a qualified noise auditor, based on an inspection of the residence, determined that\u2014 (i) the sound insulation treatment for which Federal assistance was previously provided has resulted in structural deterioration that was not caused by failure of the property owner to repair or adequately maintain the residential building or through the negligence of the applicant or the property owner; and (ii) the condition of the sound insulation treatment described in subparagraph (A) is not attributed to actions taken by an owner or occupant of the residence. (3) Additional authority for surveys Notwithstanding any other provision of law, the Secretary shall consider a cost allowable under this subchapter for an airport to conduct periodic surveys of properties in which repair and replacement of sound insulation treatment was carried out as described in paragraph (1) and for which the airport previously received Federal assistance or Federally authorized airport assistance under this subchapter. The surveys shall be conducted only for those properties for which the airport has identified a property owner who is interested in having a survey be undertaken to assess the current effectiveness of the sound insulation treatment. Such surveys shall be carried out to identify any properties described in the preceding sentence that are eligible for funds under this subsection. .",
      "versionDate": "2025-07-14",
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
        "actionDate": "2025-07-16",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2307",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Sound Insulation Treatment Repair and Replacement Program Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-10T16:45:34Z"
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
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4383ih.xml"
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
      "title": "Sound Insulation Treatment Repair and Replacement Program Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T08:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sound Insulation Treatment Repair and Replacement Program Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T08:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the establishment of pilot programs for sound insulation repair and replacement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T08:33:23Z"
    }
  ]
}
```

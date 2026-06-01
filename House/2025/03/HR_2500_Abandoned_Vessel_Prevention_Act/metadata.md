# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2500
- Title: Abandoned Vessel Prevention Act
- Congress: 119
- Bill type: HR
- Bill number: 2500
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2025-06-12T08:06:39Z
- Update date including text: 2025-06-12T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2500",
    "number": "2500",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Abandoned Vessel Prevention Act",
    "type": "HR",
    "updateDate": "2025-06-12T08:06:39Z",
    "updateDateIncludingText": "2025-06-12T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-31T20:51:40Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-31T16:02:40Z",
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
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2500ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2500\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Harder of California (for himself and Mr. Garamendi ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 46, United States Code, to assign specified liability to a person who transfers title of a commercial vessel, or former commercial vessel, to a transferee for use as a recreational vessel if the transferee does not have applicable insurance at the time of the transfer and the vessel sinks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Abandoned Vessel Prevention Act .\n#### 2. Liability for specified expenses resulting from sinking of certain decommissioned commercial vessels\n##### (a) In general\nChapter 301 of title 46, United States Code, is amended by adding at the end the following new section:\n30107. Liability for specified expenses resulting from sinking of certain decommissioned commercial vessels (a) Liability for transferor Except as provided in subsection (b), any person who transfers title of a covered vessel to another for use as a recreational vessel shall be liable for any specified expenses resulting from the vessel sinking on navigable waters of the United States. (b) Exceptions (1) Vessel length; vessel age Subsection (a) shall not apply to a vessel less than 35 feet in length or fewer than 40 years old. (2) Insurance Subsection (a) shall not apply to a person who transfers title of a covered vessel to a person who, at the time of the transfer, has insurance\u2014 (A) applicable to the vessel for the 12-month period beginning on the date of the transfer; and (B) that, in the case the vessel sinks, covers specified expenses. (c) Definitions In this section: (1) Commercial vessel The term commercial vessel has the meaning given such term in section 4462(a)(4) of the Internal Revenue Code of 1986 ( 26 U.S.C. 4462(a)(4) ). (2) Covered vessel The term covered vessel means\u2014 (A) commercial vessel; or (B) a recreational vessel that was previously a commercial vessel. (3) Specified expenses The term specified expenses mean, with respect to a sunken vessel\u2014 (A) damages attributable to the sinking of the vessel; and (B) expenses relating to\u2014 (i) removal of the vessel and any debris; (ii) clean-up of any pollution attributable to the sinking of the vessel; and (iii) any shut down of, or repairs or maintenance to, a water intake pump as a result of pollution attributable to the sinking of the vessel. (4) Recreational vessel The term recreational vessel has the meaning given such term in section 2101 of title 46, United States Code. .\n##### (b) Clerical amendment\nThe table of sections for chapter 301 of title 46, United States Code, is amended by adding at the end the following new item:\n30107. Liability for specified expenses resulting from sinking of certain decommissioned commercial vessels. .",
      "versionDate": "2025-03-31",
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
        "updateDate": "2025-04-07T14:11:16Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2500ih.xml"
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
      "title": "Abandoned Vessel Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Abandoned Vessel Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 46, United States Code, to assign specified liability to a person who transfers title of a commercial vessel, or former commercial vessel, to a transferee for use as a recreational vessel if the transferee does not have applicable insurance at the time of the transfer and the vessel sinks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:40Z"
    }
  ]
}
```

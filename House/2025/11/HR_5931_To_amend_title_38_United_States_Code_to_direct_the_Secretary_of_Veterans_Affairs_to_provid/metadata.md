# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5931?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5931
- Title: Veterans’ Cremation Certainty Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5931
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-02T09:05:46Z
- Update date including text: 2025-12-02T09:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5931",
    "number": "5931",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Veterans\u2019 Cremation Certainty Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-02T09:05:46Z",
    "updateDateIncludingText": "2025-12-02T09:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
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
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:36:39Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5931ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5931\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide direct payment to cremation providers for direct cremation designated by veterans prior to death, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans\u2019 Cremation Certainty Act of 2025 .\n#### 2. Direct payment for direct cremation\n##### (a) Direct payment for direct cremation\nChapter 23 of title 38, United States Code, is amended by adding at the end the following new section:\n2309. Direct payment for direct cremation (a) Direct payment Upon the death of an eligible veteran who has submitted an application described in subsection (b), the Secretary shall pay the direct cremation provider specified in such application the following applicable payment for the cost of direct cremation: (1) For a veteran described in section 2303(a)(2) of this title, such payment shall not exceed the amount authorized under such section and shall be in lieu of any benefit authorized under section 2302 of this title. (2) For a veteran described in section 2307 of this title, such payment shall not exceed the amount authorized under section 2307 of this title and shall be in lieu of any benefit authorized under section 2307 of this title. (b) Application An application described in this section is an application to the Secretary in which an eligible veteran elects direct cremation in lieu of benefits under section 2303 or 2307 of this title and specifies a direct cremation provider. (c) Integration with pre-Need eligibility process To the extent practicable, the Secretary shall ensure the application process under subsection (b) is integrated with the pre-need eligibility determination process (or successor process) pursuant to section 2404 of this title. (d) Definitions In this section: (1) The term direct cremation provider means a crematory or funeral home that provides direct cremation. (2) The term direct cremation means the basic cremation of human remains in a simple container without embalming, viewing, funeral ceremony, or inurnment. Such term includes\u2014 (A) transportation of the deceased from the place of death to the direct cremation provider; (B) a basic container or chosen urn; (C) delivery of the cremated remains to the next of kin or location of inurnment; and (D) completion of a death certificate. (3) The term eligible veteran means a veteran eligible for benefits under this chapter and for interment in a national cemetery under section 2402 of this title. .\n##### (b) Clerical amendment\nThe table of contents for chapter 23 of such title is amended by adding at the end the following new item:\n2309. Direct payment for direct cremation. .\n##### (c) Regulations\nNot later than 120 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall prescribe regulations under section 2309 of such title, as added by this section.\n##### (d) Application\nSection 2309 of such title, as added by this section, shall apply with respect to deaths that occur on or after the day that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2025-11-07",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-18T15:58:12Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5931ih.xml"
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
      "title": "Veterans\u2019 Cremation Certainty Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T06:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans\u2019 Cremation Certainty Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide direct payment to cremation providers for direct cremation designated by veterans prior to death, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:20Z"
    }
  ]
}
```

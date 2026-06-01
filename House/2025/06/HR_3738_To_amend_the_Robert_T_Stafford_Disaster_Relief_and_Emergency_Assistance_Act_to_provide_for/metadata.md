# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3738?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3738
- Title: HMAG Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3738
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2025-09-11T08:06:13Z
- Update date including text: 2025-09-11T08:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-05 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-05 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3738",
    "number": "3738",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "HMAG Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:13Z",
    "updateDateIncludingText": "2025-09-11T08:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
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
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-05T19:57:16Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3738ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3738\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Stanton (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide for assistance to States and local governments in response to extreme heat events, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Heat Management Assistance Grant Act of 2025 or the HMAG Act of 2025 .\n#### 2. Mitigation of extreme heat events\n##### (a) In general\nTitle IV of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 et seq. ) is amended by adding at the end the following:\n431. Mitigation of extreme heat events (a) In general The President, acting through the Regional Administrator of the Federal Emergency Management Agency, may provide assistance, including grants, equipment, supplies, and personnel, to any State or local government for the mitigation, and management of an extreme heat event. (b) Coordination In providing assistance under this section, the President shall coordinate with the head of the National Oceanic and Atmospheric Administration. (c) Eligibility To be eligible for assistance under this section, a State or local government shall submit to the President\u2014 (1) an assessment of the potential loss of life due to the extreme heat event based on information on previous events, if such events have occurred; (2) an assessment of the potential loss of revenue to such State or local government due to the extreme heat event based on any such previous event; (3) a description of any other sources of assistance available to the State or local government, including potential sources that are not solely responsible for mitigation of extreme heat events; and (4) any potential long-term impacts of the extreme heat events, including impacts to infrastructure. (d) Essential Assistance In providing assistance under this section, the President may use the authority provided under section 403. (e) Hazard Mitigation Assistance Whether or not a major disaster is declared, the President may provide hazard mitigation assistance in accordance with section 404 in any area affected by an extreme heat event for which assistance was provided under this section, including\u2014 (f) Rules and Regulations The President shall prescribe such rules and regulations as are necessary to carry out this section, including\u2014 (1) requirements for an agreement entered into by the State or local government to receive assistance under this section; (2) a procedure for an appeals process in the case of a denial of assistance requested under this section; and (3) a description of eligible costs for which assistance may be provided under this section. .\n##### (b) Development of extreme heat event threshold\nNot later than 90 days after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency, jointly with the Administrator of the National Oceanic and Atmospheric Administration and in consultation with the Director of the Centers for Disease Control and Prevention, shall develop a threshold for the temperature and duration of a heat event to qualify as an extreme heat event under section 431 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act, as added by this Act.",
      "versionDate": "2025-06-04",
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
        "name": "Emergency Management",
        "updateDate": "2025-07-15T14:50:51Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3738ih.xml"
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
      "title": "HMAG Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HMAG Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Heat Management Assistance Grant Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide for assistance to States and local governments in response to extreme heat events, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T06:48:28Z"
    }
  ]
}
```

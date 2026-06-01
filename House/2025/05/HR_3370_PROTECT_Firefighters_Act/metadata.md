# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3370?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3370
- Title: PROTECT Firefighters Act
- Congress: 119
- Bill type: HR
- Bill number: 3370
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2026-02-12T18:08:23Z
- Update date including text: 2026-02-12T18:08:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2026-02-11 18:45:24 - Floor: ASSUMING FIRST SPONSORSHIP - Ms. Houlahan asked unanimous consent that she may hereafter be considered as the first sponsor of H.R. 3370, a bill originally introduced by Representative Sherrill, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2026-02-11 18:45:24 - Floor: ASSUMING FIRST SPONSORSHIP - Ms. Houlahan asked unanimous consent that she may hereafter be considered as the first sponsor of H.R. 3370, a bill originally introduced by Representative Sherrill, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3370",
    "number": "3370",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "S001207",
        "district": "11",
        "firstName": "Mikie",
        "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
        "lastName": "Sherrill",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "PROTECT Firefighters Act",
    "type": "HR",
    "updateDate": "2026-02-12T18:08:23Z",
    "updateDateIncludingText": "2026-02-12T18:08:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2026-02-11",
      "actionTime": "18:45:24",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "ASSUMING FIRST SPONSORSHIP - Ms. Houlahan asked unanimous consent that she may hereafter be considered as the first sponsor of H.R. 3370, a bill originally introduced by Representative Sherrill, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NE"
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
      "sponsorshipDate": "2025-07-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3370ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3370\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Ms. Sherrill (for herself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo direct the United States Fire Administration to develop a comprehensive strategy to improve equipment, training, and staffing standards for firefighter Rapid Intervention Teams, including those Teams that respond to port facility fires, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Resources and Operational Training to Eliminate Crisis Threats to Firefighters Act or the PROTECT Firefighters Act .\n#### 2. Strategy to improve equipment, training, and staffing standards for rapid intervention teams\n##### (a) Strategy\n**(1) Submission**\nNot later than one year after the date of the enactment of this Act, the United States Fire Administrator shall submit to the Committee on Science, Space, and Technology and the Committee on Homeland Security of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Homeland Security and Governmental Affairs of the Senate a comprehensive strategy detailing the following:\n**(A)**\nCurrent equipment, training, and staffing standards for firefighter Rapid Intervention Teams.\n**(B)**\nHow to improve access for such Teams to modern and high-quality equipment, safety gear, training, and staffing levels.\n**(C)**\nHow to ensure equipment and training standardization and interoperability between such Teams.\n**(2) Matters**\nThe strategy under paragraph (1) shall address, at a minimum, the following:\n**(A)**\nAn identification of such training standards, firefighting equipment, and staffing level standards that, as of the date of the enactment of this Act, are in use by firefighter Rapid Intervention Teams and the extent to which such training and equipment is standard and interoperable across such Teams in each individual State and nationwide, including regarding the following:\n**(i)**\nThe frequency with which such Teams undergo training, and any financial or logistical barriers that impact such Teams\u2019 access to such training.\n**(ii)**\nThe type and quality of firefighting equipment used by such Teams and any financial or logistical barriers that impact such Teams\u2019 access to state-of-the-art firefighting equipment.\n**(iii)**\nStaffing levels and response times for such Teams, particularly for departments that are facing general firefighter staffing shortages, and any financial or logistical barriers to improving staffing levels and responses times for such Teams.\n**(iv)**\nThe level of standardization of firefighting equipment and training between such Teams across different localities and different States, a description of current State or national efforts to improve firefighting equipment and training interoperability, and any financial or logistical barriers that impact such efforts to so improve such interoperability.\n**(B)**\nAn identification of such training standards, firefighting equipment, and staffing level standards that, as of the date of the enactment of this Act, are in use by firefighter Rapid Intervention Teams at maritime and port facilities or those Teams that may be required to respond to fires at such facilities, the extent to which such training and equipment is standard and interoperable across such Teams in each individual State and nationwide, and a determination by the United States Fire Administrator regarding whether such training and equipment is sufficient to prepare such Teams for fires on the various ships that dock at such facilities, including relating to the following:\n**(i)**\nThe frequency with which such Teams undergo maritime-specific training and any financial or logistical barriers that impact such Teams\u2019 access to such training.\n**(ii)**\nThe type and quality of maritime-specific firefighting equipment used by such Teams and any financial or logistical barriers that impact such Teams\u2019 access to state-of-the-art firefighting equipment.\n**(iii)**\nStaffing levels and response times for such Teams, particularly for departments that are facing general firefighter staffing shortages, and any financial or logistical barriers to improving staffing levels and responses times for such Teams.\n**(iv)**\nThe level of standardization for interoperability of the firefighting equipment, training, and staffing levels of Teams that respond to maritime or port facility fires across different localities and different States, a description of current State or national efforts to improve such maritime-specific firefighting equipment and training interoperability, and any financial or logistical barriers that impact such efforts to so improve such interoperability.\n**(v)**\nA determination of whether the firefighting equipment, training, and staffing levels of such Teams that respond to fires at maritime and port facilities is sufficient for use on the various ships that dock at such facilities, including foreign-flagged ships that may use different firefighting equipment than that typically encountered by United States-based Teams, and a description of any financial or logistical barriers that impact fire departments\u2019 ability to make such equipment and training sufficient for such uses.\n**(C)**\nA review of the National Institute for Occupational Safety and Health\u2019s Fire Fighter Fatality Investigation and Prevention Program Line of Duty Death reports over the five-year period immediately preceding the date of the enactment of this Act that\u2014\n**(i)**\nsummarizes trends in fire departments\u2019 access to modern and high-quality firefighting equipment, safety gear, training, and staffing levels for Rapid Intervention Teams, including the level of firefighting equipment and training standardization between such Teams; and\n**(ii)**\nanalyzes the role that a lack of modern and high-quality firefighting equipment, safety gear, training, or staffing levels for Rapid Intervention Teams, including a lack of firefighting equipment and training standardization between such Teams, played in firefighter Line of Duty Deaths.\n**(D)**\nRecommendations for how Congress can expand access to modern and high-quality firefighting equipment, safety gear, training, and staffing levels for Rapid Intervention Teams and ensure firefighting equipment and training standardization between such Teams, including specific recommendations regarding how such Teams can overcome the logistical or financial barriers to improved firefighting equipment, training, and staffing identified under subparagraph (A).\n**(E)**\nRecommendations for how Congress can expand access to modern and high-quality firefighting equipment, safety gear, training, and staffing levels for Rapid Intervention Teams at maritime and port facilities or those Teams that may be required to fight fires at such facilities and ensure firefighting equipment and training standardization between such Teams, including specific recommendations regarding how such Teams can overcome the logistical or financial barriers to improved firefighting equipment, training, and staffing and any lack of sufficiency of such equipment, training, or staffing with respect to the various ships that dock at such facilities in accordance with subparagraph (B).\n**(F)**\nRecommendations for how Congress can address the specific causes of incidents in which a firefighter employed by the Federal Government, a State, or a locality was killed while in the line of duty as identified in subparagraph (C).\n##### (b) Briefing\nNot later than 18 months after the date of the enactment of this Act, the United States Fire Administrator shall provide to the Committee on Science, Space, and Technology and the Committee on Homeland Security of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Homeland Security and Governmental Affairs of the Senate a briefing on the matters covered by the strategy under subsection (a).\n##### (c) Firefighter Rapid Intervention Team defined\nIn this section, the term firefighter Rapid Intervention Team means a designated firefighting crew that serves as a stand-by rescue team at the scene of a fire or other emergency and is available for the immediate search and rescue of missing, trapped, or injured firefighters if required.",
      "versionDate": "2025-05-13",
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
            "updateDate": "2026-02-12T18:07:57Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-02-12T18:01:17Z"
          },
          {
            "name": "Fires",
            "updateDate": "2026-02-12T18:08:23Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2026-02-12T18:01:06Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-12T18:08:12Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-12T18:08:03Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-12T18:07:50Z"
          },
          {
            "name": "Navigation, waterways, harbors",
            "updateDate": "2026-02-12T18:07:03Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2026-02-12T18:07:23Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-12T18:07:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Emergency Management",
        "updateDate": "2025-06-09T14:53:45Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3370ih.xml"
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
      "title": "PROTECT Firefighters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT Firefighters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Resources and Operational Training to Eliminate Crisis Threats to Firefighters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the United States Fire Administration to develop a comprehensive strategy to improve equipment, training, and staffing standards for firefighter Rapid Intervention Teams, including those Teams that respond to port facility fires, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:23Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/47?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/47
- Title: VOICE Restoration Act
- Congress: 119
- Bill type: HR
- Bill number: 47
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-11-21T12:04:09Z
- Update date including text: 2025-11-21T12:04:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/47",
    "number": "47",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "VOICE Restoration Act",
    "type": "HR",
    "updateDate": "2025-11-21T12:04:09Z",
    "updateDateIncludingText": "2025-11-21T12:04:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:26:45Z",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr47ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 47\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Bergman introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish the Victims of Immigration Crime Engagement Office within the Department of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Victims Of Immigration Crime Engagement Restoration Act or as the VOICE Restoration Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn April 2017, the United States Department of Homeland Security launched the U.S. Immigration and Customs Enforcement (ICE) Victims of Immigration Crime Engagement Office (VOICE) in response to the Executive Order 13768 issued by President Donald J. Trump entitled Enhancing Public Safety in the Interior of the United States, which directed DHS to create an office to support victims of crimes committed by criminal aliens.\n**(2)**\nIn June 2021, the United States Department of Homeland Security terminated VOICE pursuant to the Executive order on the Revision of Civil Immigration Enforcement Policies and Priorities issued by President R. Joseph Jr.\n#### 3. Victims of Immigration Crime Engagement Office\n##### (a) Establishment\nThere is established the Victims of Immigration Crime Engagement Office (hereinafter in this Act referred to as VOICE ) within the U.S. Immigration and Customs Enforcement, which shall provide assistance to victims of crimes committed by aliens present in the United States without lawful status under the immigration laws, in addition to witnesses and legal representatives of individuals acting at the request of a victim or witness.\n##### (b) Duties\nThe duties of VOICE are to do the following:\n**(1)**\nUse a victim-centered approach to acknowledge and support persons who are victims or witnesses described in subsection (a) and their families.\n**(2)**\nPromote awareness of available services to such persons.\n**(3)**\nBuild collaborative partnerships with community stakeholders assisting such persons.\n##### (c) Assistance\nThe types of assistance authorized to be provided by VOICE to such persons impacted by crimes committed by aliens described in subsection (a) includes\u2014\n**(1)**\nthe establishment and operation of a dedicated toll-free VOICE Hotline to answer questions from victims;\n**(2)**\nlocal contacts to help with unique requests from such persons;\n**(3)**\naccess to social service professionals able to refer victims to resources and service providers;\n**(4)**\nassistance signing up to receive automated custody status information regarding an alien described in subsection (a) held in custody; and\n**(5)**\nadditional criminal or immigration history may be available about an illegal alien to victims or their families.\n##### (d) Report\nNot later than 180 days after the date of the enactment of this Act, VOICE shall publish quarterly reports to Congress, the Secretary of Homeland Security, and the President of the United States studying the effects of the victimization by aliens described in subsection (a) present in the United States.",
      "versionDate": "2025-01-03",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-06-03T18:18:53Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-06-03T18:18:53Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-06-03T18:18:53Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-06-03T18:18:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-01-31T14:18:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr47",
          "measure-number": "47",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr47v00",
            "update-date": "2025-02-06"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Victims Of Immigration Crime Engagement Restoration Act or the VOICE Restoration Act</b></p> <p>This bill establishes the Victims of Immigration Crime Engagement Office within U.S. Immigration and Customs Enforcement. The office shall provide assistance to victims of crimes committed by non-U.S. nationals (<i>aliens</i> under federal law) who are present in the United States without lawful immigration status. </p>"
        },
        "title": "VOICE Restoration Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr47.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Victims Of Immigration Crime Engagement Restoration Act or the VOICE Restoration Act</b></p> <p>This bill establishes the Victims of Immigration Crime Engagement Office within U.S. Immigration and Customs Enforcement. The office shall provide assistance to victims of crimes committed by non-U.S. nationals (<i>aliens</i> under federal law) who are present in the United States without lawful immigration status. </p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr47"
    },
    "title": "VOICE Restoration Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Victims Of Immigration Crime Engagement Restoration Act or the VOICE Restoration Act</b></p> <p>This bill establishes the Victims of Immigration Crime Engagement Office within U.S. Immigration and Customs Enforcement. The office shall provide assistance to victims of crimes committed by non-U.S. nationals (<i>aliens</i> under federal law) who are present in the United States without lawful immigration status. </p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr47"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr47ih.xml"
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
      "title": "VOICE Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T11:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VOICE Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Victims Of Immigration Crime Engagement Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Victims of Immigration Crime Engagement Office within the Department of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T11:18:27Z"
    }
  ]
}
```

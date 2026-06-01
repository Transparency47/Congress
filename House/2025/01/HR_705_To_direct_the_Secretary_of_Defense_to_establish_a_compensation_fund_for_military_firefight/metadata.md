# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/705?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/705
- Title: To direct the Secretary of Defense to establish a compensation fund for military firefighters exposed to PFAS.
- Congress: 119
- Bill type: HR
- Bill number: 705
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-10-09T03:26:23Z
- Update date including text: 2025-10-09T03:26:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/705",
    "number": "705",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001159",
        "district": "10",
        "firstName": "Marilyn",
        "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
        "lastName": "Strickland",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "To direct the Secretary of Defense to establish a compensation fund for military firefighters exposed to PFAS.",
    "type": "HR",
    "updateDate": "2025-10-09T03:26:23Z",
    "updateDateIncludingText": "2025-10-09T03:26:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sponsorshipDate": "2025-01-23",
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
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr705ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 705\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Strickland (for herself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to establish a compensation fund for military firefighters exposed to PFAS.\n#### 1. Compensation fund for military firefighters\n##### (a) Program and fund established\nNot later than two years after the date of enactment of this Act, the Secretary of Defense shall establish a program and fund to be known as the Military Firefighters Compensation Fund .\n##### (b) Purpose of program\nThe purpose of the compensation program is to provide for timely, uniform, and adequate compensation to current and former military firefighters and, where applicable, survivors of such employees, suffering from illnesses incurred by such employees in the performance of duty for the Department of Defense and certain of its contractors and subcontractors due to exposure to per- and polyfluoroalkyl substances, or PFAS.\n##### (c) PFAS exposure\nCurrent and former military firefighters shall, in the absence of substantial evidence to the contrary, be determined to have been exposed to PFAS in the performance of duty for the purposes of the compensation program if such firefighter was employed at a military installation, facility of the National Guard, of formerly used defense site during a period when PFAS would have been present at such facility.\n##### (d) Compensation provided\nA current or former military firefighter, or the survivor of such firefighter if the firefighter is deceased, shall receive compensation for the disability or death of that employee from that employee\u2019s occupational illness.\n##### (e) Payments in the case of deceased persons\n**(1) Claim filed**\nIn the case of a military firefighter who is deceased at the time of payment of compensation under this section, whether or not the death is the result of the firefighter\u2019s occupational illness, such payment may be made only as follows:\n**(A)**\nIf the military firefighter is survived by a spouse who is living at the time of payment, such payment shall be made to such surviving spouse.\n**(B)**\nIf there is no surviving spouse described in subparagraph (A), such payment shall be made in equal shares to all children of the military firefighter who are living at the time of payment.\n**(C)**\nIf there is no surviving spouse described in subparagraph (A) and if there are no children described in subparagraph (B), such payment shall be made in equal shares to the parents of the military firefighter who are living at the time of payment.\n**(D)**\nIf there is no surviving spouse described in subparagraph (A), and if there are no children described in subparagraph (B) or parents described in subparagraph (C), such payment shall be made in equal shares to all grandchildren of the military firefighter who are living at the time of payment.\n**(E)**\nIf there is no surviving spouse described in subparagraph (A), and if there are no children described in subparagraph (B), parents described in subparagraph (C), or grandchildren described in subparagraph (D), then such payment shall be made in equal shares to the grandparents of the military firefighter who are living at the time of payment.\n**(F)**\nNotwithstanding the other provisions of this paragraph, if there is\u2014\n**(i)**\na surviving spouse described in subparagraph (A); and\n**(ii)**\nat least one child of the military firefighter who is living and a minor at the time of payment and who is not a recognized natural child or adopted child of such surviving spouse, then half of such payment shall be made to such surviving spouse, and the other half of such payment shall be made in equal shares to each child of the military firefighter who is living and a minor at the time of payment.\n**(2) Before filing of claim**\nIf a current or former military firefighter eligible for payment dies before filing a claim under this section, a survivor of that firefighter who may receive payment under paragraph (1) may file a claim for such payment.\n**(3) Definitions**\nIn this subsection:\n**(A)**\nThe term child includes a recognized natural child, a stepchild who lived with an individual in a regular parent-child relationship, or an adopted child.\n**(B)**\nThe term grandchild means the child of a child of an individual.\n**(C)**\nThe term grandparent means the parent of a parent of an individual.\n**(D)**\nThe term parent includes fathers and mothers through adoption.\n**(E)**\nThe term spouse means the wife or husband of a deceased individual who was married to such individual for at least one year immediately before such death.\n##### (f) Medical benefits provided\nThe Secretary shall furnish, to an individual receiving medical benefits under this section for an illness, the services, appliances, and supplies prescribed or recommended by a qualified physician for that illness.\n##### (g) Transportation and expenses\nThe individual may be furnished necessary and reasonable transportation and expenses incident to the securing of such services, appliances, and supplies.\n##### (h) Commencement of benefits\nAn individual receiving benefits under this section shall be furnished those benefits as of the date on which that individual submitted the claim for those benefits in accordance with this section.\n##### (i) Definitions\nIn this section:\n**(1)**\nThe term military firefighter means a member of the Armed Forces or a civilian employee of the Department of Defense whose military occupational specialty or primary duties are fire suppression and prevention.\n**(2)**\nThe term military installation has the meaning given such term in section 2801(c)(4) of title 10, United States Code.\n**(3)**\nThe term PFAS means perfluoroalkyl and polyfluoroalkyl substances.\n**(4)**\nThe term perfluoroalkyl substance means a man-made chemical of which all the carbon atoms are fully fluorinated carbon atoms.\n**(5)**\nThe term polyfluoroalkyl substance means a man-made chemical with at least one fully fluorinated carbon atom and at least one nonfluorinated carbon atom.\n##### (j) Authorization for compensation fund\nThere is hereby authorized such sums as may be necessary to carry out this section.",
      "versionDate": "2025-01-23",
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
            "name": "Fires",
            "updateDate": "2025-03-20T13:53:35Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-03-20T13:53:43Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-03-20T13:53:48Z"
          },
          {
            "name": "Military civil functions",
            "updateDate": "2025-03-20T13:53:30Z"
          },
          {
            "name": "Military medicine",
            "updateDate": "2025-03-20T13:54:05Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-20T13:53:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-05T20:29:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr705",
          "measure-number": "705",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr705v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill requires the Department of Defense (DOD) to establish the Military Firefighters Compensation Fund to provide compensation to current and former military firefighters, or survivors of such firefighters, for illnesses incurred in the line of duty due to exposure to per- and polyfluoroalkyl substances, commonly known as PFAS. PFAS are man-made and may have adverse human health effects.</p><p>Under the bill, current and former military firefighters are presumed to have been exposed to PFAS (in the absence of substantial evidence to the contrary) if the firefighter was employed at a military installation, facility of the National Guard, or formerly used defense site during a period when PFAS would have been present at such facility.</p><p>The bill provides that in cases where a military firefighter is deceased at the time of payment of compensation, the surviving spouse must receive the payment. If there is no surviving spouse, the bill provides for the order of distribution to other surviving parties (e.g., a child or parent of the firefighter). The bill also provides that a survivor of a firefighter may file a claim for compensation if the firefighter dies before filing a claim.</p><p>DOD must furnish the services, appliances, and supplies prescribed or recommended to a military firefighter who is receiving medical benefits for an illness related to PFAS exposure. Additionally, such firefighter\u00a0may be furnished necessary and reasonable transportation and expenses incident to securing care for such illness.</p>"
        },
        "title": "To direct the Secretary of Defense to establish a compensation fund for military firefighters exposed to PFAS."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr705.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Department of Defense (DOD) to establish the Military Firefighters Compensation Fund to provide compensation to current and former military firefighters, or survivors of such firefighters, for illnesses incurred in the line of duty due to exposure to per- and polyfluoroalkyl substances, commonly known as PFAS. PFAS are man-made and may have adverse human health effects.</p><p>Under the bill, current and former military firefighters are presumed to have been exposed to PFAS (in the absence of substantial evidence to the contrary) if the firefighter was employed at a military installation, facility of the National Guard, or formerly used defense site during a period when PFAS would have been present at such facility.</p><p>The bill provides that in cases where a military firefighter is deceased at the time of payment of compensation, the surviving spouse must receive the payment. If there is no surviving spouse, the bill provides for the order of distribution to other surviving parties (e.g., a child or parent of the firefighter). The bill also provides that a survivor of a firefighter may file a claim for compensation if the firefighter dies before filing a claim.</p><p>DOD must furnish the services, appliances, and supplies prescribed or recommended to a military firefighter who is receiving medical benefits for an illness related to PFAS exposure. Additionally, such firefighter\u00a0may be furnished necessary and reasonable transportation and expenses incident to securing care for such illness.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr705"
    },
    "title": "To direct the Secretary of Defense to establish a compensation fund for military firefighters exposed to PFAS."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Department of Defense (DOD) to establish the Military Firefighters Compensation Fund to provide compensation to current and former military firefighters, or survivors of such firefighters, for illnesses incurred in the line of duty due to exposure to per- and polyfluoroalkyl substances, commonly known as PFAS. PFAS are man-made and may have adverse human health effects.</p><p>Under the bill, current and former military firefighters are presumed to have been exposed to PFAS (in the absence of substantial evidence to the contrary) if the firefighter was employed at a military installation, facility of the National Guard, or formerly used defense site during a period when PFAS would have been present at such facility.</p><p>The bill provides that in cases where a military firefighter is deceased at the time of payment of compensation, the surviving spouse must receive the payment. If there is no surviving spouse, the bill provides for the order of distribution to other surviving parties (e.g., a child or parent of the firefighter). The bill also provides that a survivor of a firefighter may file a claim for compensation if the firefighter dies before filing a claim.</p><p>DOD must furnish the services, appliances, and supplies prescribed or recommended to a military firefighter who is receiving medical benefits for an illness related to PFAS exposure. Additionally, such firefighter\u00a0may be furnished necessary and reasonable transportation and expenses incident to securing care for such illness.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr705"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr705ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to establish a compensation fund for military firefighters exposed to PFAS.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:18:35Z"
    },
    {
      "title": "To direct the Secretary of Defense to establish a compensation fund for military firefighters exposed to PFAS.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T09:05:24Z"
    }
  ]
}
```

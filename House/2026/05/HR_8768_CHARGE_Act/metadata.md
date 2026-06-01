# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8768?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8768
- Title: CHARGE Act
- Congress: 119
- Bill type: HR
- Bill number: 8768
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-21T19:35:57Z
- Update date including text: 2026-05-21T19:35:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8768",
    "number": "8768",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "CHARGE Act",
    "type": "HR",
    "updateDate": "2026-05-21T19:35:57Z",
    "updateDateIncludingText": "2026-05-21T19:35:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:04:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8768ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8768\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Mr. Self introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title 49, United States Code, to include certain electric vehicles or related equipment manufactured by, and services provided by, a foreign entity of concern to the noncomplying motor vehicles list, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cybersecurity and Hardware Assurance for Resilient Grid Electrification Act or the CHARGE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nChina accounts for two thirds of the global electric vehicle market.\n**(2)**\nElectric vehicles from China are not currently within the United States automotive market, but that is expected to increase to 8 percent of the market by 2030.\n**(3)**\nBy 2030, 20 percent of new vehicle sales are expected to need a connection to the electrical grid.\n**(4)**\nVehicle manufacturers routinely update and maintain vehicle software remotely without oversight.\n**(5)**\nAccording to the Department of Energy, local power outages cost the United States $121,000,000,000 annually and result in a 1.3 percent reduction in GDP.\n**(6)**\nOn April 28, 2025, the electrical grid that services large portions of Spain and Portugal failed to maintain frequency and voltage resulting in a 16-hour nationwide blackout, the largest power failure in Europe in over 20 years.\n**(7)**\nFailure of any of the electrical grids of the United States for 3 days could reduce the GDP of the United States by up to 2.6 percent.\n**(8)**\nThe Vehicle to Grid (VTG) Initiative connects electrical vehicle batteries to the grid as a renewable source of power during peak loads and then replaces that power during times of low demand.\n**(9)**\nA vehicle connected to the electrical grid, through the VTG program, retains unique control of the availability of the battery of such vehicle with respect to energy provision supply.\n**(10)**\nFast switching of battery availability while connected to the electrical grid may hamper the ability of the electrical grid to maintain the standard 60 Hz frequency and 120V/240V household service voltage resulting in deviations which may damage devices that are plugged in, both residential and commercial.\n**(11)**\nA coordinated attack by an array of participating vehicles from adversarial manufacturers would make the grid vulnerable to possible manipulation and disruptions.\n**(12)**\nA failure of the electric grid of the United States would damage electric vehicles connected to the electric grid and hamper safety efforts to protect our national security, patrol the streets of cities in the United States, and maintain law and order, while also putting life-saving health services at risk.\n#### 3. Inclusion of certain vehicles and equipment manufactured by China on the noncomplying motor vehicles list\n##### (a) Definitions\nSection 30102(a) of title 49, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraphs (5) through (13) as paragraphs (7) through (15), respectively;\n**(2)**\nby inserting after paragraph (4) the following new paragraphs:\n(5) electric vehicle has the meaning given the term in section 32904(a)(2). (6) foreign entity of concern has the meaning given the term in section 9901 of title XCIX of division H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ). ; and\n**(3)**\nby adding at the end the following new paragraph:\n(16) vehicle charge power control component means an onboard electrical and electronic system that regulates, converts, and manages the flow of energy between the energy port of a vehicle and the traction battery of a vehicle, including an onboard charger, a power-electronic converter, a battery-management control, and an associated high-voltage protection device. .\n##### (b) Prohibitions on manufacturing, selling, and importing noncomplying motor vehicles and equipment\nSection 30112(a) of title 49, United States Code, is amended by adding at the end the following new paragraph:\n(4) Except as provided in this section, section 30114, subsections (i) and (j) of section 30120, and subchapter III of this chapter, a person may not sell, offer for sale, introduce or deliver for introduction in interstate commerce, or import into the United States any motor vehicle or motor vehicle equipment if the vehicle or equipment\u2014 (A) is an electric vehicle or equipment of an electric vehicle manufactured in whole or in part by a foreign entity of concern; or (B) uses a vehicle charge power control component manufactured in whole or in part by a foreign entity of concern. .",
      "versionDate": "2026-05-12",
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
        "updateDate": "2026-05-21T19:35:56Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8768ih.xml"
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
      "title": "CHARGE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T03:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHARGE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T03:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cybersecurity and Hardware Assurance for Resilient Grid Electrification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T03:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to include certain electric vehicles or related equipment manufactured by, and services provided by, a foreign entity of concern to the noncomplying motor vehicles list, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T03:18:40Z"
    }
  ]
}
```

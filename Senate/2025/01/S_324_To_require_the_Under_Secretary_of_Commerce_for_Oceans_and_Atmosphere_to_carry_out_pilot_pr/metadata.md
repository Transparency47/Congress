# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/324?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/324
- Title: Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 324
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-04-17T18:59:00Z
- Update date including text: 2025-04-17T18:59:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/324",
    "number": "324",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacklyn",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025",
    "type": "S",
    "updateDate": "2025-04-17T18:59:00Z",
    "updateDateIncludingText": "2025-04-17T18:59:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-01-30T00:08:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "CA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s324is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 324\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Ms. Rosen (for herself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Under Secretary of Commerce for Oceans and Atmosphere to carry out pilot projects relating to improved subseasonal to seasonal forecasting in agriculture and water management, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025 .\n#### 2. Weather and climate information in agriculture and water management\nSection 1762 of the Food Security Act of 1985 ( 15 U.S.C. 8521 ) is amended\u2014\n**(1)**\nby amending subsection (h) to read as follows:\n(h) Subseasonal to seasonal forecasting pilot projects (1) Establishment The Under Secretary shall establish not fewer than two pilot projects, in accordance with paragraph (2), within the U.S. Weather Research Program of the Oceanic and Atmospheric Research office of the National Oceanic and Atmospheric Administration to support improved subseasonal to seasonal precipitation forecasts for the following: (A) Water management in the western United States. (B) Agriculture in the United States. (2) Objectives In carrying out this subsection, the Under Secretary shall ensure the following: (A) A pilot project under subparagraph (A) of paragraph (1) addresses key science challenges to improving forecasts and developing related products for water management in the western United States, including the following: (i) Improving operational model resolution, both horizontal and vertical, to resolve issues associated with mountainous terrain, such as intensity of precipitation and relative fraction of rain versus snow precipitation. (ii) Improving fidelity in the operational modeling of the atmospheric boundary layer in mountainous regions. (iii) Resolving challenges in predicting winter atmospheric circulation and storm tracks, including periods of blocked versus unblocked flow over the eastern North Pacific Ocean and western United States. (iv) Improving the forecast of atmospheric rivers. (v) Improving\u2014 (I) the quality and temporal and spatial resolution of observations of air-sea interactions; (II) operational modeling of air-sea interactions; and (III) operational modeling of the influence of oceans on subseasonal and seasonal forecasting. (B) A pilot project under subparagraph (B) of paragraph (1) addresses key science challenges to improving forecasts and developing related products for agriculture in the United States, including the following: (i) Improving the quality and temporal and spatial resolution of observations and accurate operational modeling of the land surface and hydrologic cycle, including soil moisture and flash drought processes. (ii) Improving fidelity in the operational modeling of warm season precipitation processes. (iii) Understanding and predicting large-scale upper-level dynamical flow anomalies that occur in spring and summer. (3) Activities A pilot project under this subsection shall include activities that\u2014 (A) best implement recommendations contained in the 2020 report of the National Weather Service, entitled Subseasonal and Seasonal Forecasting Innovation: Plans for the Twenty-First Century ; (B) achieve measurable objectives for operational forecast improvement; (C) engage with, and leverage the resources of, institutions of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )), or a consortia thereof, and entities within the National Oceanic and Atmospheric Administration in existence as of the date of the enactment of this subsection, including Regional Climate Centers and the National Centers for Environmental Information; and (D) are carried out in coordination with the Assistant Administrator for the Office of Oceanic and Atmospheric Research and the Director of the National Weather Service. (4) Sunset The authority under this subsection shall terminate on the date that is five years after the date of the enactment of this subsection. ; and\n**(2)**\nby amending subsection (j) to read as follows:\n(j) Authorization of appropriations There are authorized to be appropriated $45,000,000 for each of fiscal years 2025 through 2029 to carry out the activities under this section. .",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-07T15:51:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
    "originChamber": "Senate",
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
          "measure-id": "id119s324",
          "measure-number": "324",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s324v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025</strong></p><p>This bill directs the National Oceanic and Atmospheric Administration (NOAA) to establish pilot projects to support improved subseasonal to seasonal precipitation forecasting for water management in the western United States and for agriculture nationwide. (Under current law, <em>subseasonal</em> means the time range between two weeks and three months, and <em>seasonal</em> means the time range between three months and two years.)</p><p>Specifically, NOAA must establish a pilot project to address challenges to improving forecasting and related product development for water management in the western United States. The project must address, among other items, improvements to operational modeling in mountainous regions and to the forecasting of atmospheric rivers.\u00a0</p><p>NOAA must also establish a second pilot project to address challenges to improving forecasting and related product development for U.S. agriculture. The project must address, among other items, improvements to operational modeling of warm-season precipitation and to the prediction of certain spring and summer weather patterns. \u00a0</p><p>Each pilot project must include activities that engage with and leverage the resources of academic institutions and entities within NOAA, and that achieve measurable objectives for operational forecast improvement. NOAA\u2019s authority with respect to these pilot projects expires five years after the bill\u2019s enactment.\u00a0</p>"
        },
        "title": "Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s324.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025</strong></p><p>This bill directs the National Oceanic and Atmospheric Administration (NOAA) to establish pilot projects to support improved subseasonal to seasonal precipitation forecasting for water management in the western United States and for agriculture nationwide. (Under current law, <em>subseasonal</em> means the time range between two weeks and three months, and <em>seasonal</em> means the time range between three months and two years.)</p><p>Specifically, NOAA must establish a pilot project to address challenges to improving forecasting and related product development for water management in the western United States. The project must address, among other items, improvements to operational modeling in mountainous regions and to the forecasting of atmospheric rivers.\u00a0</p><p>NOAA must also establish a second pilot project to address challenges to improving forecasting and related product development for U.S. agriculture. The project must address, among other items, improvements to operational modeling of warm-season precipitation and to the prediction of certain spring and summer weather patterns. \u00a0</p><p>Each pilot project must include activities that engage with and leverage the resources of academic institutions and entities within NOAA, and that achieve measurable objectives for operational forecast improvement. NOAA\u2019s authority with respect to these pilot projects expires five years after the bill\u2019s enactment.\u00a0</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s324"
    },
    "title": "Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025</strong></p><p>This bill directs the National Oceanic and Atmospheric Administration (NOAA) to establish pilot projects to support improved subseasonal to seasonal precipitation forecasting for water management in the western United States and for agriculture nationwide. (Under current law, <em>subseasonal</em> means the time range between two weeks and three months, and <em>seasonal</em> means the time range between three months and two years.)</p><p>Specifically, NOAA must establish a pilot project to address challenges to improving forecasting and related product development for water management in the western United States. The project must address, among other items, improvements to operational modeling in mountainous regions and to the forecasting of atmospheric rivers.\u00a0</p><p>NOAA must also establish a second pilot project to address challenges to improving forecasting and related product development for U.S. agriculture. The project must address, among other items, improvements to operational modeling of warm-season precipitation and to the prediction of certain spring and summer weather patterns. \u00a0</p><p>Each pilot project must include activities that engage with and leverage the resources of academic institutions and entities within NOAA, and that achieve measurable objectives for operational forecast improvement. NOAA\u2019s authority with respect to these pilot projects expires five years after the bill\u2019s enactment.\u00a0</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s324"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s324is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Smarter Weather Forecasting for Water Management, Farming, and Ranching Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Under Secretary of Commerce for Oceans and Atmosphere to carry out pilot projects relating to improved subseasonal to seasonal forecasting in agriculture and water management, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:29Z"
    }
  ]
}
```

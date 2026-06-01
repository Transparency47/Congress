# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7762?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7762
- Title: Protecting Our Produce Act
- Congress: 119
- Bill type: HR
- Bill number: 7762
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-03-20T15:09:36Z
- Update date including text: 2026-03-20T15:09:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7762",
    "number": "7762",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B000490",
        "district": "2",
        "firstName": "Sanford",
        "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
        "lastName": "Bishop",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Protecting Our Produce Act",
    "type": "HR",
    "updateDate": "2026-03-20T15:09:36Z",
    "updateDateIncludingText": "2026-03-20T15:09:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7762ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7762\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Bishop introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Specialty Crops Competitiveness Act of 2004 to require the Secretary of Agriculture to establish a pilot program to provide recovery payments to producers of seasonal and perishable crops that experience low prices caused by imports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Produce Act .\n#### 2. Seasonal and perishable crop loss pilot program\nThe Specialty Crops Competitiveness Act of 2004 ( Public Law 108\u2013465 ; 118 Stat. 3882) is amended\u2014\n**(1)**\nby striking Secretary of Agriculture each place it appears and inserting Secretary ;\n**(2)**\nin section 3 ( 7 U.S.C. 1621 note)\u2014\n**(A)**\nin paragraph (3), by striking (3) The term and inserting the following:\n(4) State department of agriculture The term ;\n**(B)**\nin paragraph (2), by striking (2) The term and inserting the following:\n(3) State The term ; and\n**(C)**\nin paragraph (1), by striking (1) The term and inserting the following:\n(1) Secretary The term Secretary means the Secretary of Agriculture. (2) Specialty crop The term ; and\n**(3)**\nby adding at the end the following:\nV Seasonal and perishable crop programs 501. Seasonal and perishable crop loss pilot program (a) Definitions In this section: (1) Effective price The term effective price , with respect to a seasonal and perishable crop for a marketing year, means the national average market price for that seasonal and perishable crop during the seasonal marketing window for the seasonal and perishable crop. (2) Reference price The term reference price , with respect to a seasonal and perishable crop for a marketing year, means the average of the national average market prices received by all producers of the seasonal and perishable crop during the seasonal marketing window for the seasonal and perishable crop for the most recent 5-year period of marketing seasons, excluding\u2014 (A) the marketing season during that period with the highest national average market price; and (B) the marketing season during that period with the lowest national average market price. (3) Seasonal and perishable crop The term seasonal and perishable crop means an asparagus, bell pepper, blueberry, cucumber, or squash crop that is\u2014 (A) marketed in raw form for consumption without further processing; and (B) as determined by the Secretary, normally marketed not later than 4 weeks after harvesting. (4) Seasonal marketing window The term seasonal marketing window means the timeframe during a marketing year, as determined by the Secretary\u2014 (A) during which a crop is normally marketed within a specific geographical region of the United States; and (B) that concludes on the date that is not later than 4 weeks after the last day on which the crop is normally harvested. (b) Establishment of pilot program (1) In general Beginning with marketing year 2025, the Secretary shall establish a pilot program under which the Secretary shall provide annual crop loss payments to producers of seasonal and perishable crops located in any geographical region described in paragraph (2) in accordance with this section, if the Secretary determines that, during the applicable marketing year\u2014 (A) the effective price of the seasonal and perishable crop is less than the reference price of that seasonal and perishable crop; and (B) the crop loss described in subparagraph (A) is caused by imports of the applicable seasonal and perishable crop. (2) Description of geographical regions A geographical region referred to in paragraph (1) is a geographical region of the United States in which a seasonal and perishable crop is grown within a seasonal marketing window during which a harvest and shipment of the seasonal and perishable crop occurs, as determined by the Secretary. (c) Eligibility (1) Application To be eligible to receive a payment under the pilot program under this section, a producer of 1 or more seasonal and perishable crops shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including the information described in paragraph (2). (2) Requirement No producer may be eligible to receive a payment under the pilot program under this section unless the producer\u2014 (A) has an average adjusted gross income of less than $5,000,000 for the 3 tax years preceding the most recent tax year; and (B) derives at least 75 percent of the adjusted gross income of the producer from farming, ranching, or forestry, as determined by the Secretary. (d) Payment amount The amount of a payment provided under the pilot program under this section shall be equal to the product obtained by multiplying\u2014 (1) the payment rate for the marketing year for which the payment is provided with respect to the applicable seasonal and perishable crop under subsection (e); and (2) the average production during the 5 most recent marketing years of the seasonal and perishable crop by the producer during the seasonal marketing window, excluding\u2014 (A) the marketing year during that period with the highest production; and (B) the marketing year during that period with the lowest production. (e) Payment rate The rate of a payment provided under the pilot program under this section shall be equal to the difference between\u2014 (1) the reference price of the applicable seasonal and perishable crop; and (2) the effective price of that seasonal and perishable crop. (f) Sunset The pilot program under this section shall terminate on the date that is 5 years after the date of enactment of the Protecting Our Produce Act . (g) Authorization of appropriations There is authorized to carry out the pilot program under this section $200,000,000 for each fiscal year that begins after the date of the enactment of the Protecting Our Produce Act and before the date described in subsection (f). .",
      "versionDate": "2026-03-03",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-20T15:09:35Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7762ih.xml"
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
      "title": "Protecting Our Produce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T08:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Produce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T08:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Specialty Crops Competitiveness Act of 2004 to require the Secretary of Agriculture to establish a pilot program to provide recovery payments to producers of seasonal and perishable crops that experience low prices caused by imports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T08:03:27Z"
    }
  ]
}
```

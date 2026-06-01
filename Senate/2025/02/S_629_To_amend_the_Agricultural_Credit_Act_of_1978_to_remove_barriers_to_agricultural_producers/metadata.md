# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/629?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/629
- Title: Emergency Conservation Program Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 629
- Origin chamber: Senate
- Introduced date: 2025-02-19
- Update date: 2026-04-15T12:33:37Z
- Update date including text: 2026-04-15T12:33:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-19: Introduced in Senate
- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2026-03-24 - Floor: Message on Senate action sent to the House.
- 2026-03-24 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S1565; text: CR S1565)
- 2026-03-24 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-03-24 - Discharge: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.
- 2026-03-24 - Committee: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.
- 2026-03-24 14:02:29 - Floor: Received in the House.
- 2026-03-24 14:11:22 - Floor: Held at the desk.
- Latest action: 2025-02-19: Introduced in Senate

## Actions

- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2026-03-24 - Floor: Message on Senate action sent to the House.
- 2026-03-24 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S1565; text: CR S1565)
- 2026-03-24 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-03-24 - Discharge: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.
- 2026-03-24 - Committee: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.
- 2026-03-24 14:02:29 - Floor: Received in the House.
- 2026-03-24 14:11:22 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-19",
    "latestAction": {
      "actionDate": "2025-02-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/629",
    "number": "629",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Emergency Conservation Program Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-04-15T12:33:37Z",
    "updateDateIncludingText": "2026-04-15T12:33:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-03-24",
      "actionTime": "14:11:22",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-03-24",
      "actionTime": "14:02:29",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S1565; text: CR S1565)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-24",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-03-24",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-19",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-19",
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
        "item": [
          {
            "date": "2026-03-24T16:55:39Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-02-19T19:32:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s629is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 629\nIN THE SENATE OF THE UNITED STATES\nFebruary 19, 2025 Mrs. Fischer (for herself, Mr. Luj\u00e1n , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Credit Act of 1978 to remove barriers to agricultural producers in accessing funds to carry out emergency measures under the emergency conservation program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Emergency Conservation Program Improvement Act of 2025 .\n#### 2. Improving the Emergency Conservation Program\nSection 401 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2201 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin the subsection heading, by inserting and other emergency conservation measures after fencing ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby inserting or for other emergency measures to replace or restore farmland or conservation structures requiring an immediate response (as determined by the Secretary), after replacement of fencing, ; and\n**(ii)**\nby striking option of receiving and all that follows through the period at the end and inserting the following:\noption of receiving, before the agricultural producer carries out the repair, replacement, or restoration\u2014 (A) with respect to a payment to the agricultural producer for a replacement, 75 percent of the cost of the replacement, as determined by the Secretary; and (B) with respect to a payment to the agricultural producer for a repair or restoration, 50 percent of the cost of the repair or restoration, as determined by the Secretary. ; and\n**(C)**\nin paragraph (2), by striking 60-day and inserting 180-day ; and\n**(2)**\nby adding at the end the following:\n(c) Wildfire determination A wildfire that causes damage eligible for a payment under subsection (a) includes\u2014 (1) a wildfire that is not caused naturally, if the damage is caused by the spread of the wildfire due to natural causes; and (2) a wildfire that is caused by the Federal Government. .\n#### 3. Improving the Emergency Forest Restoration Program\nSection 407 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2206 ) is amended\u2014\n**(1)**\nin subsection (a)(2), by striking wildfires, and inserting wildfires (including a wildfire that is not caused naturally, if the damage is caused by the spread of the wildfire due to natural causes, and a wildfire that is caused by the Federal Government), ;\n**(2)**\nby redesignating subsection (e) as subsection (f); and\n**(3)**\nby inserting after subsection (d) the following:\n(e) Advance payments (1) In general The Secretary shall give an owner of nonindustrial private forest land the option of receiving, before the owner carries out emergency measures under this section, not more than 75 percent of the cost of the emergency measures, as determined by the Secretary. (2) Return of funds If the funds provided under paragraph (1) are not expended by the end of the 180-day period beginning on the date on which the owner of nonindustrial private forest land receives those funds, the funds shall be returned within a reasonable timeframe, as determined by the Secretary. .",
      "versionDate": "2025-02-19",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s629es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 629\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Agricultural Credit Act of 1978 to remove barriers to agricultural producers in accessing funds to carry out emergency measures under the emergency conservation program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Emergency Conservation Program Improvement Act of 2025 .\n#### 2. Improving the Emergency Conservation Program\nSection 401 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2201 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin the subsection heading, by inserting and other emergency conservation measures after fencing ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby inserting or for other emergency measures to replace or restore farmland or conservation structures requiring an immediate response (as determined by the Secretary), after replacement of fencing, ; and\n**(ii)**\nby striking option of receiving and all that follows through the period at the end and inserting the following:\noption of receiving, before the agricultural producer carries out the repair, replacement, or restoration\u2014 (A) with respect to a payment to the agricultural producer for a replacement, 75 percent of the cost of the replacement, as determined by the Secretary; and (B) with respect to a payment to the agricultural producer for a repair or restoration, 50 percent of the cost of the repair or restoration, as determined by the Secretary. ; and\n**(C)**\nin paragraph (2), by striking 60-day and inserting 180-day ; and\n**(2)**\nby adding at the end the following:\n(c) Wildfire determination A wildfire that causes damage eligible for a payment under subsection (a) includes\u2014 (1) a wildfire that is not caused naturally, if the damage is caused by the spread of the wildfire due to natural causes; and (2) a wildfire that is caused by the Federal Government. .\n#### 3. Improving the Emergency Forest Restoration Program\nSection 407 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2206 ) is amended\u2014\n**(1)**\nin subsection (a)(2), by striking wildfires, and inserting wildfires (including a wildfire that is not caused naturally, if the damage is caused by the spread of the wildfire due to natural causes, and a wildfire that is caused by the Federal Government), ;\n**(2)**\nby redesignating subsection (e) as subsection (f); and\n**(3)**\nby inserting after subsection (d) the following:\n(e) Advance payments (1) In general The Secretary shall give an owner of nonindustrial private forest land the option of receiving, before the owner carries out emergency measures under this section, not more than 75 percent of the cost of the emergency measures, as determined by the Secretary. (2) Return of funds If the funds provided under paragraph (1) are not expended by the end of the 180-day period beginning on the date on which the owner of nonindustrial private forest land receives those funds, the funds shall be returned within a reasonable timeframe, as determined by the Secretary. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Agricultural prices, subsidies, credit",
            "updateDate": "2026-03-26T15:47:31Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2026-03-26T15:47:31Z"
          },
          {
            "name": "Farmland",
            "updateDate": "2026-04-15T12:33:37Z"
          },
          {
            "name": "Fires",
            "updateDate": "2026-03-26T15:47:31Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-03-26T15:47:31Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2026-03-26T15:47:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T14:04:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-19",
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
          "measure-id": "id119s629",
          "measure-number": "629",
          "measure-type": "s",
          "orig-publish-date": "2025-02-19",
          "originChamber": "SENATE",
          "update-date": "2026-01-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s629v00",
            "update-date": "2026-01-29"
          },
          "action-date": "2025-02-19",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Emergency Conservation Program Improvement Act of 2025 </strong></p><p>This bill revises the Emergency Conservation Program (ECP) and the Emergency Forest Restoration Program (EFRP) to expand eligibility for payments to agricultural producers and owners of forest land impacted by natural disasters. The bill also\u00a0provides additional options to receive an advance on cost-sharing payments before carrying out emergency measures.</p><p>The bill expands advance ECP payments to include\u00a0the replacement, repair, or restoration of farmland or conservation structures requiring an immediate response. Producers may receive an advance on cost-sharing payments for 75% of the cost of the replacement and 50% of the cost of the repair or restoration. Current law limits advance payments to 25% of the cost of the repair or replacement of fencing.</p><p>Under EFRP, the bill allows owners of nonindustrial private forest land impacted by a natural disaster to receive an advance on cost-sharing payments for up to 75% of the cost of the emergency measures. Currently, advance payments are not available under the program.</p><p>ECP and EFRP recipients must use the funds within 180 days after the funds are disbursed. This provides additional time to ECP recipients who currently must use the funds within 60 days.</p><p>The bill also expands eligibility for payments under the programs to include emergency measures to address damages caused by (1) a wildfire that is not caused naturally, if the damage is caused by the spread of the wildfire due to natural causes; and (2) a wildfire that is caused by the federal government.</p>"
        },
        "title": "Emergency Conservation Program Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s629.xml",
    "summary": {
      "actionDate": "2025-02-19",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Emergency Conservation Program Improvement Act of 2025 </strong></p><p>This bill revises the Emergency Conservation Program (ECP) and the Emergency Forest Restoration Program (EFRP) to expand eligibility for payments to agricultural producers and owners of forest land impacted by natural disasters. The bill also\u00a0provides additional options to receive an advance on cost-sharing payments before carrying out emergency measures.</p><p>The bill expands advance ECP payments to include\u00a0the replacement, repair, or restoration of farmland or conservation structures requiring an immediate response. Producers may receive an advance on cost-sharing payments for 75% of the cost of the replacement and 50% of the cost of the repair or restoration. Current law limits advance payments to 25% of the cost of the repair or replacement of fencing.</p><p>Under EFRP, the bill allows owners of nonindustrial private forest land impacted by a natural disaster to receive an advance on cost-sharing payments for up to 75% of the cost of the emergency measures. Currently, advance payments are not available under the program.</p><p>ECP and EFRP recipients must use the funds within 180 days after the funds are disbursed. This provides additional time to ECP recipients who currently must use the funds within 60 days.</p><p>The bill also expands eligibility for payments under the programs to include emergency measures to address damages caused by (1) a wildfire that is not caused naturally, if the damage is caused by the spread of the wildfire due to natural causes; and (2) a wildfire that is caused by the federal government.</p>",
      "updateDate": "2026-01-29",
      "versionCode": "id119s629"
    },
    "title": "Emergency Conservation Program Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-19",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Emergency Conservation Program Improvement Act of 2025 </strong></p><p>This bill revises the Emergency Conservation Program (ECP) and the Emergency Forest Restoration Program (EFRP) to expand eligibility for payments to agricultural producers and owners of forest land impacted by natural disasters. The bill also\u00a0provides additional options to receive an advance on cost-sharing payments before carrying out emergency measures.</p><p>The bill expands advance ECP payments to include\u00a0the replacement, repair, or restoration of farmland or conservation structures requiring an immediate response. Producers may receive an advance on cost-sharing payments for 75% of the cost of the replacement and 50% of the cost of the repair or restoration. Current law limits advance payments to 25% of the cost of the repair or replacement of fencing.</p><p>Under EFRP, the bill allows owners of nonindustrial private forest land impacted by a natural disaster to receive an advance on cost-sharing payments for up to 75% of the cost of the emergency measures. Currently, advance payments are not available under the program.</p><p>ECP and EFRP recipients must use the funds within 180 days after the funds are disbursed. This provides additional time to ECP recipients who currently must use the funds within 60 days.</p><p>The bill also expands eligibility for payments under the programs to include emergency measures to address damages caused by (1) a wildfire that is not caused naturally, if the damage is caused by the spread of the wildfire due to natural causes; and (2) a wildfire that is caused by the federal government.</p>",
      "updateDate": "2026-01-29",
      "versionCode": "id119s629"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s629is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s629es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Emergency Conservation Program Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T10:58:20Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Emergency Conservation Program Improvement Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-03-25T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Emergency Conservation Program Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Credit Act of 1978 to remove barriers to agricultural producers in accessing funds to carry out emergency measures under the emergency conservation program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:01Z"
    }
  ]
}
```

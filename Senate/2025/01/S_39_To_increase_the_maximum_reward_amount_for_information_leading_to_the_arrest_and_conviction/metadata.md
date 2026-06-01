# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/39?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/39
- Title: STOP MADURO Act
- Congress: 119
- Bill type: S
- Bill number: 39
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-12-05T22:49:18Z
- Update date including text: 2025-12-05T22:49:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/39",
    "number": "39",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "STOP MADURO Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:18Z",
    "updateDateIncludingText": "2025-12-05T22:49:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T19:41:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "LA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NE"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s39is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 39\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Scott of Florida (for himself, Mr. Cruz , Mr. Cassidy , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo increase the maximum reward amount for information leading to the arrest and conviction of Nicol\u00e1s Maduro Moros to $100,000,000, which shall be paid out by the Federal Government from all assets being withheld from Nicol\u00e1s Maduro Moros, officials of the Maduro regime and their co-conspirators.\n#### 1. Short titles\nThis Act may be cited as the Securing Timely Opportunities for Payment and Maximizing Awards for Detaining Unlawful Regime Officials Act of 2025 or the STOP MADURO Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 2020, the Trump administration charged Venezuela regime leader Nicol\u00e1s Maduro Moros, along with other regime officials with\u2014\n**(A)**\nparticipating in a narco-terrorism conspiracy, which carries a 20-year mandatory minimum sentence and a maximum sentence of life in prison;\n**(B)**\nconspiring to import cocaine into the United States, which carries a 10-year mandatory minimum sentence and a maximum sentence of life in prison;\n**(C)**\nusing and carrying machine guns and destructive devices during, and in relation to, and possessing machine guns and destructive devices in furtherance of, the narco-terrorism and cocaine-importation conspiracies, which carries a 30-year mandatory minimum sentence and a maximum sentence of life in prison; and\n**(D)**\nconspiring to use and carry machine guns and destructive devices during, and in relation to, and to possess machine guns and destructive devices in furtherance of, the narco-terrorism and cocaine-importation conspiracies, which carries a maximum sentence of life in prison.\n**(2)**\nOn March 26, 2020, United States Attorney Geoffrey S. Berman of the Southern District of New York stated in a press release, Today we announce criminal charges against Nicol\u00e1s Maduro for running, together with his top lieutenants, a narco-terrorism partnership with the FARC for the past twenty years. The scope and magnitude of the drug trafficking alleged was made possible only because Maduro and others corrupted the institutions of Venezuela and provided political and military protection for the rampant narco-terrorism crimes described in our charges. As alleged, Maduro and the other defendants expressly intended to flood the United States with cocaine in order to undermine the health and well-being of our nation. Maduro very deliberately deployed cocaine as a weapon. .\n**(3)**\nThe press release included a statement from United States Attorney Ariana Fajardo Orshan of the Southern District of Florida, who stated, In the last couple of years, the U.S. Attorney\u2019s Office in South Florida and its Federal law enforcement partners have united to bring dozens of criminal charges against high-level regime officials and co-conspirators resulting in seizures of approximately $450 million dollars. .\n#### 3. Increasing the maximum reward amount for information leading to the arrest and conviction of Nicol\u00e1s Maduro Moros through the Department of State rewards program\n##### (a) Authorization\nNotwithstanding section 36(e)(1) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2708(e)(1) ), the Secretary of State may pay, to one or more individuals who furnish information described in section 36(b) of such Act that directly leads to the arrest and conviction of Nicol\u00e1s Maduro Moros, a reward of up to $100,000,000.\n##### (b) Source of funds\nThe payment authorized under subsection (a) shall be derived exclusively from the liquidation of assets being withheld from Nicol\u00e1s Maduro Moros, officials of the Maduro regime, and their co-conspirators by the President or by the Office of Foreign Assets Control of the Department of the Treasury pursuant to\u2014\n**(1)**\nthe Foreign Narcotics Kingpin Designation Act ( 21 U.S.C. 1901 et seq. );\n**(2)**\nsection 5 of the Venezuela Defense of Human Rights and Civil Society Act of 2014 ( 50 U.S.C. 1701 note);\n**(3)**\nExecutive Order 13692 ( 50 U.S.C. 1701 note; relating to blocking of property and suspending entry of certain persons contributing to the situation in Venezuela);\n**(4)**\nExecutive Order 13850 (relating to blocking property of additional persons contributing to the situation in Venezuela);\n**(5)**\nExecutive Order 13884 ( 50 U.S.C. 1701 note; relating to blocking property of the Government of Venezuela); or\n**(6)**\nany other sanctions provision.",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-09",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "268",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STOP MADURO Act",
      "type": "HR"
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
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-09-17T20:03:02Z"
          },
          {
            "name": "Department of State",
            "updateDate": "2025-09-17T20:03:02Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-09-17T20:03:02Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-09-17T20:03:02Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2025-09-17T20:03:02Z"
          },
          {
            "name": "Latin America",
            "updateDate": "2025-09-17T20:03:02Z"
          },
          {
            "name": "Venezuela",
            "updateDate": "2025-09-17T20:03:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-02-19T18:32:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119s39",
          "measure-number": "39",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s39v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Securing Timely Opportunities for Payment and Maximizing Awards for Detaining Unlawful Regime Officials Act of 2025 or the STOP MADURO Act</strong></p><p>This bill authorizes the Department of State to pay a reward of up to $100 million for certain information directly leading to the arrest and conviction of Nicolas\u00a0Maduro Moros.</p><p>For example,\u00a0under the bill, the State Department may pay such a reward to one or more individuals who furnish information directly leading to Maduro's arrest and conviction in any country for specified narcotics-related offenses.</p><p>The bill also requires that any such payment come solely from the liquidation of assets that the U.S. President or the Department of the Treasury's Office of Foreign Assets Control has withheld pursuant to specified laws and executive orders from Maduro, officials of the Maduro regime, and their co-conspirators.</p>"
        },
        "title": "STOP MADURO Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s39.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Securing Timely Opportunities for Payment and Maximizing Awards for Detaining Unlawful Regime Officials Act of 2025 or the STOP MADURO Act</strong></p><p>This bill authorizes the Department of State to pay a reward of up to $100 million for certain information directly leading to the arrest and conviction of Nicolas\u00a0Maduro Moros.</p><p>For example,\u00a0under the bill, the State Department may pay such a reward to one or more individuals who furnish information directly leading to Maduro's arrest and conviction in any country for specified narcotics-related offenses.</p><p>The bill also requires that any such payment come solely from the liquidation of assets that the U.S. President or the Department of the Treasury's Office of Foreign Assets Control has withheld pursuant to specified laws and executive orders from Maduro, officials of the Maduro regime, and their co-conspirators.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119s39"
    },
    "title": "STOP MADURO Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Securing Timely Opportunities for Payment and Maximizing Awards for Detaining Unlawful Regime Officials Act of 2025 or the STOP MADURO Act</strong></p><p>This bill authorizes the Department of State to pay a reward of up to $100 million for certain information directly leading to the arrest and conviction of Nicolas\u00a0Maduro Moros.</p><p>For example,\u00a0under the bill, the State Department may pay such a reward to one or more individuals who furnish information directly leading to Maduro's arrest and conviction in any country for specified narcotics-related offenses.</p><p>The bill also requires that any such payment come solely from the liquidation of assets that the U.S. President or the Department of the Treasury's Office of Foreign Assets Control has withheld pursuant to specified laws and executive orders from Maduro, officials of the Maduro regime, and their co-conspirators.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119s39"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s39is.xml"
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
      "title": "STOP MADURO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STOP MADURO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing Timely Opportunities for Payment and Maximizing Awards for Detaining Unlawful Regime Officials Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase the maximum reward amount for information leading to the arrest and conviction of Nicolas Maduro Moros to $100,000,000, which shall be paid out by the Federal Government from all assets being withheld from Nicolas Maduro Moros, officials of the Maduro regime and their co-conspirators.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:25Z"
    }
  ]
}
```

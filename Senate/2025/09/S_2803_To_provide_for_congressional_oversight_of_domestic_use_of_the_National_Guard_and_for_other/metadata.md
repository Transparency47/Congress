# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2803?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2803
- Title: SUN Act
- Congress: 119
- Bill type: S
- Bill number: 2803
- Origin chamber: Senate
- Introduced date: 2025-09-15
- Update date: 2025-12-09T12:03:19Z
- Update date including text: 2025-12-09T12:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in Senate
- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-09-15: Introduced in Senate

## Actions

- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2803",
    "number": "2803",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SUN Act",
    "type": "S",
    "updateDate": "2025-12-09T12:03:19Z",
    "updateDateIncludingText": "2025-12-09T12:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-15",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-16T00:07:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "IL"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "IL"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MD"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NM"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-08",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2803is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2803\nIN THE SENATE OF THE UNITED STATES\nSeptember 15, 2025 Mr. Padilla (for himself, Mr. Schiff , Mr. Durbin , Ms. Duckworth , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide for congressional oversight of domestic use of the National Guard, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding the Use of the National Guard Act or the SUN Act .\n#### 2. Congressional oversight of domestic use of the National Guard\n##### (a) In general\nExcept as provided in subsection (b), not later than 15 days after the date on which the President deploys or otherwise uses members of the National Guard at a location in the United States pursuant to chapter 13 or 15 of title 10, United States Code, or any other law or authority, the President shall submit to Congress a report on the use or deployment that includes\u2014\n**(1)**\nthe precise legal basis and goals of the President for the deployment or other use, including any evidence substantiating the assessment of the President;\n**(2)**\na description of the effect of such deployment or use on any situation identified in such justification, including any specific reports of any interactions between members of the National Guard and civilians engaged in violence or threats of violence;\n**(3)**\nreports from local and State law enforcement agencies describing any such interactions, including the extent of actual violence or threat of violence, and the assessment of such agencies of the propriety of deployment or other use of members of the National Guard;\n**(4)**\nan estimate of the total cost to the Federal Government for the entirety of the deployment or use, including any indirect costs to the Department of Defense; and\n**(5)**\na certification that such deployment or use of the members of the National Guard will not interfere with the ability of the Armed Forces to respond in the event of a disaster that could be covered by a presidential declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ).\n##### (b) Exception\nSubsection (a) shall not apply with respect to the use or deployment of members of the National Guard at a location in the United States pursuant to a presidential declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) in response to a natural disaster or other weather-related event.",
      "versionDate": "2025-09-15",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-29T18:26:47Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2803is.xml"
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
      "title": "SUN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SUN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safeguarding the Use of the National Guard Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for congressional oversight of domestic use of the National Guard, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:20Z"
    }
  ]
}
```

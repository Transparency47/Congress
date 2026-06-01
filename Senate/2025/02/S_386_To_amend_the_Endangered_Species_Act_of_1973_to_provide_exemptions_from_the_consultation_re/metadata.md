# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/386?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/386
- Title: Critical Water Resources Prioritization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 386
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2025-05-13T19:44:17Z
- Update date including text: 2025-05-13T19:44:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/386",
    "number": "386",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Critical Water Resources Prioritization Act of 2025",
    "type": "S",
    "updateDate": "2025-05-13T19:44:17Z",
    "updateDateIncludingText": "2025-05-13T19:44:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T19:31:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "WY"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s386is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 386\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Ms. Lummis (for herself, Mr. Barrasso , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Endangered Species Act of 1973 to provide exemptions from the consultation requirements required under that Act for agency actions that fulfill critical human water needs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Critical Water Resources Prioritization Act of 2025 .\n#### 2. Critical water resources exemptions under the Endangered Species Act of 1973\n##### (a) In general\nSection 7 of the Endangered Species Act of 1973 ( 16 U.S.C. 1536 ) is amended by adding at the end the following:\n(q) Human needs exemptions for water resources (1) Definitions In this subsection: (A) Critical human water need The term critical human water need means water required\u2014 (i) for a municipal drinking water supply; (ii) for emergency services, including firefighting; (iii) to maintain public health and safety, as determined by the Secretary or a relevant water management agency; or (iv) for food security, as determined by the Secretary. (B) Water management agency The term water management agency means any Federal, State, or local agency with authority to manage or allocate water resources. (2) Exemptions for critical human water needs Notwithstanding any other provision of this Act, the Secretary may grant an exemption from the requirements of subsection (a)(2) for any agency action carried out by a water management agency to fulfill a critical human water need if\u2014 (A) those requirements would directly conflict with the fulfillment of the critical human water need; (B) the water management agency has\u2014 (i) implemented all reasonable water conservation measures; (ii) explored all feasible alternative water sources; and (iii) determined no other reasonable alternatives exist to meet the critical human water need; and (C) the water management agency submits to the Secretary\u2014 (i) documentation of the conditions described in subparagraphs (A) and (B); (ii) a plan to minimize adverse impacts on affected species; and (iii) a timeline for reinstating those requirements. (3) Duration and renewal (A) Initial period An exemption granted by the Secretary under paragraph (2) shall be valid for a period of not more than 180 days. (B) Renewal The Secretary may renew an exemption under paragraph (2) for additional 180-day periods if the conditions described in subparagraphs (A) and (B) of paragraph (2) continue to exist and the applicable water management agency resubmits the information described in subparagraph (C) of that paragraph. (4) Reports (A) Water management agency reports A water management agency operating under an exemption granted under paragraph (2) shall submit to the Secretary monthly reports describing\u2014 (i) the ongoing critical human water need for which the exemption was made; (ii) efforts to develop alternative water sources; and (iii) (I) impacts on affected species; and (II) measures taken to minimize those impacts. (B) Secretary reports The Secretary shall submit to Congress an annual report describing\u2014 (i) all exemption made under this subsection; (ii) the cumulative impact of those exemptions on affected species; and (iii) recommendations for improving the balance between critical human water needs and species protection. (5) Judicial review Any action taken under this subsection shall be subject to judicial review only for arbitrary and capricious agency action under section 706 of title 5, United States Code. .\n##### (b) Regulations\nNot later than 180 days after the date of enactment of this Act, the Secretary (as defined in section 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 )) shall promulgate regulations to implement the amendments made by this section.",
      "versionDate": "2025-02-04",
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
        "name": "Environmental Protection",
        "updateDate": "2025-05-13T19:44:17Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s386is.xml"
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
      "title": "Critical Water Resources Prioritization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T03:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Critical Water Resources Prioritization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Endangered Species Act of 1973 to provide exemptions from the consultation requirements required under that Act for agency actions that fulfill critical human water needs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:33Z"
    }
  ]
}
```

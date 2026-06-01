# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3324?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3324
- Title: FERC Greenhouse Gas and Environmental Justice Policy Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3324
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3324",
    "number": "3324",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "FERC Greenhouse Gas and Environmental Justice Policy Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T18:37:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "DE"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3324is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3324\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mr. Durbin (for himself, Ms. Blunt Rochester , Ms. Duckworth , Mr. Markey , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo confirm and clarify the Federal Energy Regulatory Commission\u2019s obligation to assess and mitigate the impacts to climate change and environmental justice communities from projects approved pursuant to the Natural Gas Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FERC Greenhouse Gas and Environmental Justice Policy Act of 2025 .\n#### 2. Greenhouse gas and environmental justice policy\n##### (a) Mitigation proposal\nSection 7(d) of the Natural Gas Act ( 15 U.S.C. 717f(d) ) is amended by inserting , including a mitigation proposal described in subsection (i)(3), after contain such information .\n##### (b) Present or future public convenience and necessity determination\nSection 7 of the Natural Gas Act ( 15 U.S.C. 717f ) is amended by adding at the end the following:\n(i) Present or future public convenience and necessity determination (1) In general In finding whether a proposed action, to the extent that may be authorized by a certificate, is or will be required by the present or future public convenience and necessity under subsection (e), the Commission shall determine whether\u2014 (A) the environmental effects of such proposed action, including any effects relating to the environment of such proposed action on environmental justice communities, are significant, and if such significant environmental effects, if any, can be mitigated pursuant to a mitigation proposal required under subsection (d); (B) the significant environmental effects of the proposed action outweigh the benefits of the proposed action under paragraph (4); and (C) the proposed action is necessary to ensure energy reliability and affordability. (2) Significant environmental effects (A) In general In determining whether the environmental effects of a proposed action are significant under paragraph (1)(A), the Commission shall, with respect to such proposed action\u2014 (i) evaluate such environmental effects on environmental justice communities under subparagraph (B); and (ii) quantify reasonably foreseeable greenhouse gas emissions resulting from such proposed action under subparagraph (C). (B) Environmental justice communities The Commission shall evaluate the effects of a proposed action on environmental justice communities based on all evidence in the record, including\u2014 (i) existing environmental and public health stressors; (ii) any adverse environmental and public health stressors resulting from the proposed action; (iii) the presence or absence of adverse cumulative stressors; (iv) potential environmental and public health stressors associated with the proposed action; and (v) other factors, as identified by the Commission and the affected environmental justice communities following a meaningful opportunity for public engagement by those communities. (C) Quantification of greenhouse gas emissions The Commission shall quantify reasonably foreseeable greenhouse gas emissions resulting from a proposed action based on all evidence in the record, including\u2014 (i) the projected capacity of the relevant pipelines to transport natural gas; (ii) the projected utilization rate of the relevant pipelines; (iii) the construction and operation of the proposed action; (iv) the projected downstream greenhouse gas emissions and effects, including cumulative effects, on environmental justice communities resulting from the proposed action, including those resulting from the combustion of the natural gas; (v) the projected upstream greenhouse gas emissions and effects, including cumulative effects, on environmental justice communities resulting from the proposed action, including those resulting from leakage or other release of the natural gas; and (vi) other factors, as identified by the Commission. (D) Threshold For purposes of determining whether the environmental effects of a proposed action are significant under this paragraph, the Commission shall\u2014 (i) with respect to environmental effects described in subparagraph (B), consider that\u2014 (I) no community should bear a disproportionate share of the adverse environmental and public health consequences that results from the Commission approving an application for a certificate of public convenience or necessity; and (II) it is in the public interest for the Commission, where appropriate, to limit the future placement and expansion of a proposed action in environmental justice communities; and (ii) with respect to quantifying greenhouse gas emissions under subparagraph (C), presume\u2014 (I) a proposed action that has reasonably foreseeable emissions of at least 100,000 metric tons per year of carbon dioxide equivalent to have a significant effect on climate change; and (II) greenhouse gases other than carbon dioxide shall be converted to carbon dioxide equivalent using the 20-year global warming potentials from the most recent assessment report published by the Intergovernmental Panel on Climate Change. (3) Mitigation (A) In general Under subsection (d), the Commission shall require an applicant for a certificate to submit a proposal with the applicable application that details how the applicant will mitigate all or a portion of the environmental effects of the proposed action, including on climate change and environmental justice communities. (B) Conditions Upon reviewing the mitigation proposal under subparagraph (A), the Commission shall, to the extent practicable, attach to the issuance of a certificate, and to the exercise of the rights granted thereunder, conditions that require the holder of such certificate to address any potential adverse effects of any action authorized under such certificate on climate change and environmental justice communities. (C) Additional requirement For any proposed action the Commission approves for which it does not require conditions that mitigate or offset the significant environmental effects of the proposed action to below the significance threshold described in paragraph (2)(D), the Commission shall provide a detailed explanation as to why such mitigation is not practicable. (4) Weighing (A) In general Under paragraph (1)(B), the Commission shall weigh all environmental effects, including significant environmental effects, to the extent any significant environmental effects can be practicably mitigated under the threshold described in paragraph (2)(D) and determine whether the benefits of the proposed action outweigh such environmental effects. (B) Limitation In the event the Commission finds that the proposed action is or will be required by the present or future public convenience and necessity under subsection (e) despite any significant environmental effects that cannot be practicably mitigated, the Commission shall provide a detailed explanation as to why the Commission finds the proposed action to be nevertheless required by the present or future public convenience and necessity. (5) Definitions In this subsection: (A) Certificate The term certificate means a certificate of public convenience and necessity described in subsection (c). (B) Environmental effect The term environmental effect means an effect caused by a proposed action on the environment and climate change. (C) Environmental justice community The term environmental justice community means any population of color, community of color, indigenous community, or low-income community that experiences a disproportionate burden of the negative human health and environmental impacts of pollution or other environmental hazards. (D) Proposed action The term proposed action means a proposed service, sale, operation, construction, extension, or acquisition, as described in subsection (e), in an application for a certificate. .",
      "versionDate": "2025-12-03",
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
        "actionDate": "2025-12-03",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6378",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FERC Greenhouse Gas and Environmental Justice Policy Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2026-01-05T16:09:18Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3324is.xml"
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
      "title": "FERC Greenhouse Gas and Environmental Justice Policy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-24T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FERC Greenhouse Gas and Environmental Justice Policy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to confirm and clarify the Federal Energy Regulatory Commission's obligation to assess and mitigate the impacts to climate change and environmental justice communities from projects approved pursuant to the Natural Gas Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T03:48:18Z"
    }
  ]
}
```

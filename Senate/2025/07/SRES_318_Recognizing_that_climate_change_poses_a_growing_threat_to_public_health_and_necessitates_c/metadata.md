# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/318?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/318
- Title: A resolution recognizing that climate change poses a growing threat to public health and necessitates coordinated action to mitigate its impacts and safeguard the health and well-being of all people in the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 318
- Origin chamber: Senate
- Introduced date: 2025-07-10
- Update date: 2025-12-05T22:02:34Z
- Update date including text: 2025-12-05T22:02:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in Senate
- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S4318-4319)
- Latest action: 2025-07-10: Introduced in Senate

## Actions

- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S4318-4319)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/318",
    "number": "318",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A resolution recognizing that climate change poses a growing threat to public health and necessitates coordinated action to mitigate its impacts and safeguard the health and well-being of all people in the United States.",
    "type": "SRES",
    "updateDate": "2025-12-05T22:02:34Z",
    "updateDateIncludingText": "2025-12-05T22:02:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S4318-4319)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T18:02:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sponsorshipDate": "2025-07-10",
      "state": "DE"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres318is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 318\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mr. Markey (for himself, Ms. Blunt Rochester , Mr. Merkley , Mr. Van Hollen , and Mr. Booker ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nRecognizing that climate change poses a growing threat to public health and necessitates coordinated action to mitigate its impacts and safeguard the health and well-being of all people in the United States.\nThat it is the sense of the Senate that\u2014\n**(1)**\nthe Department of Health and Human Services should use all practicable means and measures to increase the health sector\u2019s climate readiness and response, including increasing the ability to withstand and maintain operations during extreme weather events, strengthening the climate resilience of health infrastructure and supply chains, and lowering the sector\u2019s environmental impact;\n**(2)**\nfunding appropriated by Congress to facilitate energy efficiency retrofits, investments in clean vehicles and onsite renewable energy and storage, and planning for climate resilience projects by health care organizations and community-based organizations should be distributed without delay and with particular attention to historically underserved communities and organizations by the responsible Federal agencies;\n**(3)**\nthe Department of Health and Human Services should prioritize technical assistance, capacity building, and equitable access to funding for Tribal health systems, rural hospitals and clinics, and historically underresourced health care providers to support climate adaptation and preparedness;\n**(4)**\nFederal agencies with responsibilities for public health, health care, and environmental data, including the Department of Health and Human Services, should orchestrate and support efforts to close information gaps and synthesize data on the health impacts of climate change, including mitigation and adaptation strategies, and use that information to develop timely, targeted, accessible, and evidence-based education and communication tools on climate-related health threats;\n**(5)**\nthe Department of Health and Human Services should fully reinstate the Office of Climate Change and Health Equity and the Office of Environmental Justice with the staffing and resources necessary to lead and coordinate departmental efforts, guide equitable implementation, and use all available levers to address the health impacts of climate change for all people in the United States, and particularly for those most at risk;\n**(6)**\ncritical agencies, staff, and programmatic functions necessary to support the goal of reducing the health impacts of climate change should be fully funded, reinstated, and supported, including\u2014\n**(A)**\nthose within the Administration for Children and Families;\n**(B)**\nthe Administration for Strategic Preparedness and Response;\n**(C)**\nthe Agency for Healthcare Research and Quality;\n**(D)**\nthe Indian Health Service;\n**(E)**\nthose within the Centers for Disease Control and Prevention, such as the National Center for Environmental Health, the Agency for Toxic Substances and Disease Registry, and the National Institute for Occupational Safety and Health; and\n**(F)**\nthose within the National Institutes of Health, including the Climate Change and Health Initiative;\n**(7)**\ninvestments in climate resilience and health infrastructure should include support for\u2014\n**(A)**\nworkforce training, job quality standards, and equitable access to careers in public health;\n**(B)**\nemergency preparedness and energy and environmental response, particularly for workers from historically underserved communities; and\n**(C)**\ncommunity-led mental wellness and resilience building initiatives and mutual aid networks;\n**(8)**\nrelevant Federal agencies, including the Department of Health and Human Services, should ensure community-based organizations, Tribal governments, and environmental justice groups are meaningfully engaged in climate-health decision-making processes, and are provided with the resources and authority necessary to lead and support local resilience efforts, including public health preparedness, infrastructure adaptation, emergency response planning, support for psychological and emotional well-being, and efforts to address climate-related health disparities;\n**(9)**\nthe Department of Labor, through the Occupational Safety and Health Administration, should promulgate a worker heat protection standard that, in accordance with the best available evidence, establishes the maximum protective program of measures an employer shall implement to regulate employees\u2019 exposure to heat stress and prevent heat-related illness and injury that attains the highest degree of health and safety protection to the extent feasible; and\n**(10)**\nthe Department of Health and Human Services and other relevant Federal agencies should provide annual progress reports to Congress and the public on climate resilience investments, measurable health outcomes, and equitable distribution of resources to vulnerable populations and regions.",
      "versionDate": "2025-07-10",
      "versionType": "IS"
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
        "actionDate": "2025-07-10",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Natural Resources, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "568",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing that climate change poses a growing threat to public health and necessitates coordinated action to mitigate its impacts and safeguard the health and well-being of all people in the United States.",
      "type": "HRES"
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
        "name": "Health",
        "updateDate": "2025-07-24T13:01:32Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres318is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution recognizing that climate change poses a growing threat to public health and necessitates coordinated action to mitigate its impacts and safeguard the health and well-being of all people in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-12T02:18:21Z"
    },
    {
      "title": "A resolution recognizing that climate change poses a growing threat to public health and necessitates coordinated action to mitigate its impacts and safeguard the health and well-being of all people in the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-11T10:56:19Z"
    }
  ]
}
```

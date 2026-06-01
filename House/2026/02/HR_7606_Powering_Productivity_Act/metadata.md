# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7606?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7606
- Title: Powering Productivity Act
- Congress: 119
- Bill type: HR
- Bill number: 7606
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-02-25T17:29:24Z
- Update date including text: 2026-02-25T17:29:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7606",
    "number": "7606",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Powering Productivity Act",
    "type": "HR",
    "updateDate": "2026-02-25T17:29:24Z",
    "updateDateIncludingText": "2026-02-25T17:29:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
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
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:34:05Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "FL"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7606ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7606\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Casten (for himself, Ms. Castor of Florida , and Mr. Cleaver ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo study and accelerate the more productive use of energy resources within the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Powering Productivity Act .\n#### 2. Purpose\nThe purpose of this Act is to improve the energy performance, transparency, and decision-making of the United States by modernizing how the United States measures and accounts for energy productivity and related impacts.\n#### 3. Energy productivity assessments\n##### (a) National energy productivity baseline\nNot later than 18 months after the date of enactment of this Act, the Secretary of Energy, in consultation with the Task Force, shall publish a comprehensive baseline assessment of energy productivity in the United States, which shall, at a minimum\u2014\n**(1)**\ndefine a framework and methodology for measuring energy productivity as the relationship between energy inputs and the economic or societal value of the work performed by those inputs, at the national, regional, and sectoral levels;\n**(2)**\nevaluate current energy productivity performance at the national, regional, and sectoral levels;\n**(3)**\nidentify barriers to improved energy productivity across economic sectors; and\n**(4)**\nhighlight opportunities for improvement through technology, policy, behavioral, or structural interventions.\n##### (b) Periodic energy productivity indicators quarterly report\nUpon publication of the baseline assessment under subsection (a), and at least quarterly thereafter, the Administrator of the Energy Information Administration shall publish a report on energy productivity in the United States, to be known as the Energy Productivity Indicators Quarterly or Energy Productivity-IQ . Each Energy Productivity-IQ shall measure energy productivity using the same measures of economic output, by sector and nationally, as those used in the labor productivity estimates published by the Bureau of Labor Statistics in its Productivity and Costs reports, or any successor publication that reports such estimates. The Administrator of the Energy Information Administration shall coordinate with the Secretary of Labor to align, to the extent practicable, the publication schedule of the Energy Productivity-IQ with the publication schedule of the Bureau of Labor Statistics Productivity and Costs reports, or any successor publication that reports estimates of labor productivity.\n##### (c) Comprehensive energy productivity and competitiveness assessment\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, and every three years thereafter, the Secretary of Energy shall produce a Comprehensive Energy Productivity and Competitiveness Assessment using existing Federal modeling tools and data systems. The assessment shall\u2014\n**(A)**\nquantify the direct and indirect economic, environmental, health, and societal impacts of achieving accelerated energy productivity improvements, relative to a business-as-usual scenario, at the national, regional, and sectoral levels;\n**(B)**\nanalyze potential policy pathways to enhance competitiveness, reduce energy costs, increase resilience, and support job creation;\n**(C)**\nevaluate how such improvements affect national and regional well-being, including reductions in pollution, energy costs, public health burdens, water use, and economic vulnerability;\n**(D)**\ndetail how improvements in energy productivity in the United States affect competitiveness in key economic sectors, including manufacturing, services, and other energy-intensive industries;\n**(E)**\nevaluate risks associated with delayed action, including stranded asset exposure and competitiveness losses;\n**(F)**\ninclude, as appropriate, recommendations for Federal policies, programs, and research priorities to support sustained energy productivity gains; and\n**(G)**\ninclude, as appropriate, supporting data, modeling scenarios, investment implications, and additional information to support increased American competitiveness through improved energy productivity.\n**(2) Consideration of lifecycle factors**\nIn carrying out each assessment under this subsection, the Secretary of Energy shall consider how lifecycle factors associated with energy production, delivery, and use affect energy productivity, system costs, resilience, and economic competitiveness, including through impacts on\u2014\n**(A)**\nwater resources, including withdrawals, consumption, and water quality;\n**(B)**\npublic health outcomes, including exposure to pollution and associated health burdens;\n**(C)**\nmaterial use, supply chain constraints, and waste generation;\n**(D)**\nemissions and other environmental impacts that materially affect economic or societal outcomes; and\n**(E)**\ndirect and indirect economic impacts, including effects on energy costs, productivity, employment, and regional competitiveness.\n#### 4. Development of energy productivity and cost task force\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary of Energy shall establish an advisory group, to be known as the Energy Productivity Task Force , which shall be led by the Secretary of Energy.\n##### (b) Membership\n**(1) Federal agencies**\nThe Task Force shall include representatives from the following:\n**(A)**\nThe Department of Energy.\n**(B)**\nThe Department of Commerce.\n**(C)**\nThe Environmental Protection Agency.\n**(D)**\nThe Energy Information Administration.\n**(E)**\nThe Federal Energy Regulatory Commission.\n**(F)**\nThe National Oceanic and Atmospheric Administration.\n**(G)**\nThe United States Geological Survey.\n**(H)**\nThe Department of Health and Human Services.\n**(I)**\nThe Office of Science and Technology Policy.\n**(2) Independent experts**\nIn addition to the representatives from Federal agencies described in paragraph (1), the Secretary shall appoint independent technical experts and stakeholders from industry, academia, and public-interest organizations, which shall consist of stakeholders that represent\u2014\n**(A)**\nthe electric power sector;\n**(B)**\nthe renewable energy sector;\n**(C)**\nthe nonrenewable energy sector;\n**(D)**\nconsumer advocacy groups;\n**(E)**\nenergy-intensive industries;\n**(F)**\nenvironmental and public interest advocacy organizations;\n**(G)**\nthe National Academies of Sciences, Engineering, and Medicine;\n**(H)**\nacademic- and National Laboratory-based researchers with expertise in\u2014\n**(i)**\nenergy and economics;\n**(ii)**\nclimate and economics; or\n**(iii)**\nenvironmental systems and economics; and\n**(I)**\nany other sector or organization the Secretary of Energy determines relevant for the purposes of this Act.\n##### (c) Termination\nNotwithstanding section 1013 of title 5, United States Code, the Task Force shall terminate on the date that is 3 years after the date of enactment of this section.\n#### 5. Definitions\nIn this Act:\n**(1) Energy productivity**\nThe term energy productivity means a measure of how efficiently an economy, region, or industry uses energy to generate economic value.\n**(1) Task force**\nThe term Task Force means the Energy Productivity Task Force established under section 4.",
      "versionDate": "2026-02-20",
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
        "name": "Energy",
        "updateDate": "2026-02-25T17:29:23Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7606ih.xml"
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
      "title": "Powering Productivity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T09:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Powering Productivity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To study and accelerate the more productive use of energy resources within the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T09:18:34Z"
    }
  ]
}
```

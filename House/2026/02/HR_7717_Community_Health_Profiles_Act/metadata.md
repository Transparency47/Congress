# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7717?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7717
- Title: Community Health Profiles Act
- Congress: 119
- Bill type: HR
- Bill number: 7717
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-03-27T20:08:14Z
- Update date including text: 2026-03-27T20:08:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7717",
    "number": "7717",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Community Health Profiles Act",
    "type": "HR",
    "updateDate": "2026-03-27T20:08:14Z",
    "updateDateIncludingText": "2026-03-27T20:08:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:05:10Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7717ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7717\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Torres of New York introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish a pilot program at the Centers for Disease Control and Prevention to support local jurisdictions in developing neighborhood-level, publicly accessible health data platforms, to establish a National Neighborhood Health Data Repository, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Health Profiles Act .\n#### 2. Community health data pilot program\n##### (a) Establishment\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention (in this section referred to as the Secretary ), shall establish a pilot program (in this section referred to as the Program ) to award grants, on a competitive basis, to not more than 25 eligible entities to develop or enhance neighborhood-level, publicly accessible health data platforms. Such platforms shall submit de-identified, aggregated data to the National Neighborhood Health Data Repository established under subsection (h), consistent with applicable Federal, State, and local privacy laws.\n##### (b) Program objectives\nThe objectives of the Program shall be to\u2014\n**(1)**\npromote equitable access to local health data;\n**(2)**\nsupport the integration of Federal, State, and local surveillance systems into user-friendly, publicly accessible health data platforms;\n**(3)**\nfacilitate data-driven public health planning and community engagement;\n**(4)**\nprovide actionable insights at the State and local level, with a focus on addressing health disparities; and\n**(5)**\nsupport the establishment and maintenance of the National Neighborhood Health Data Repository to enable national comparability while upholding local data privacy standards.\n##### (c) Eligible entities\nTo be eligible for a grant under the Program, an entity shall be\u2014\n**(1)**\na State or local health department; or\n**(2)**\na municipality or county government.\n##### (d) Partnership with academic and nonprofit institutions\nIn administering a grant under the Program, an eligible entity may partner with an academic or nonprofit institution.\n##### (e) Priority\nIn awarding grants under the Program, the Secretary\u2014\n**(1)**\nshall prioritize eligible entities that\u2014\n**(A)**\nserve populations experiencing health disparities, such as medically underserved communities, low-income communities, or environmentally burdened communities;\n**(B)**\nlack a neighborhood-level, publicly accessible health data system; and\n**(C)**\ndemonstrate plans to use the data collected from such a system to reduce health disparities; and\n**(2)**\nmay prioritize eligible entities that propose innovative indicators beyond traditional public health surveillance (pursuant to subsection (f)(1)).\n##### (f) Use of funds\nA grant under the Program may only be used to\u2014\n**(1)**\ndevelop or expand a publicly accessible health data platform to provide neighborhood-level data across key domains, including\u2014\n**(A)**\nsocial and economic conditions, such as education, economic stress, neighborhood, violence, and incarceration;\n**(B)**\nhousing and neighborhood conditions, such as the prevalence and quality of air conditioners, housing quality, and the quality of the built environment;\n**(C)**\nmaternal and child health;\n**(D)**\nhealthy living, such as self-reported health status;\n**(E)**\nhealth care, such as access to care and avoidable hospitalization and vaccination; and\n**(F)**\nhealth outcomes, such as chronic conditions, the prevalence or treatment of human immunodeficiency virus (commonly known as HIV ) and Hepatitis C, binge drinking and psychiatric hospitalizations, infant mortality and premature death, and life expectancy;\n**(2)**\nintegrate data from multiple sources, including\u2014\n**(A)**\nFederal surveillance systems;\n**(B)**\nState and local administrative survey data; and\n**(C)**\nlocal education, housing, and public safety data;\n**(3)**\nensure data disaggregation by neighborhood, ZIP code, or census tract, and support comparability across local jurisdictions where feasible;\n**(4)**\ndesign neighborhood-level, publicly accessible health data platforms with clear citation of sources and transparent methodology;\n**(5)**\nincorporate into such platforms\u2014\n**(A)**\nvisualization tools, such as charts, maps, and trend lines; and\n**(B)**\ndownloadable datasets for public use;\n**(6)**\nprovide training or technical assistance to community and local institutions to ensure sustainability and usability of such platforms, including assistance in aligning such platforms with Federal interoperability standards and model legal frameworks for privacy, confidentiality, and data-sharing compliance; and\n**(7)**\nsubmit de-identified, aggregated data collected or generated using grant funds under the Program to the National Neighborhood Health Data Repository, in such standardized format as the Secretary may require.\n##### (g) Administration and evaluation\n**(1) Administration**\nIn administering the Program, the Secretary shall\u2014\n**(A)**\nissue program guidance and technical assistance for platform development, data integration, and public accessibility, including\u2014\n**(i)**\nstandards for secure data reporting to the National Neighborhood Health Data Repository and alignment with Federal, State, and local laws; and\n**(ii)**\nmodel provisions on confidentiality and comparability;\n**(B)**\nprovide technical assistance to grant recipients on data methodology, privacy protection, and system interoperability; and\n**(C)**\nfacilitate collaboration and peer learning among grant recipients to share best practices and promote replicability.\n**(2) Evaluation**\n**(A) Initial report**\nNot later than 1 year after the establishment of the Program, the Secretary shall submit to Congress a report that\u2014\n**(i)**\nsummarizes the outcomes of the Program and the progress made on the development of neighborhood-level, publicly accessible health data platforms;\n**(ii)**\nassesses improvements the Program has made in public access to health data, data usability, and community engagement; and\n**(iii)**\nidentifies lessons learned and makes recommendations for whether and how the Program could be expanded nationally or extended beyond the 4-year termination period described in subsection (k).\n**(B) Updates**\nThe Secretary may update or supplement the report described in subparagraph (A) as the Secretary determines appropriate.\n##### (h) National Neighborhood Health Data Repository\n**(1) Establishment**\nThe Secretary shall establish and maintain a publicly accessible, searchable National Neighborhood Health Data Repository to aggregate de-identified, neighborhood-level health data from recipients of grants under the Program.\n**(2) Elements**\nThe Repository shall\u2014\n**(A)**\ndisplay data submitted by recipients of grants under the Program;\n**(B)**\nenable comparisons across local jurisdictions; and\n**(C)**\ninclude tools for visualization, filtering, and downloading of data.\n**(3) Oversight**\nThe Secretary shall provide oversight of the Repository by\u2014\n**(A)**\nreviewing data submissions;\n**(B)**\ndeveloping and implementing a methodology for the aggregation of health data as described in paragraph (4); and\n**(C)**\nin consultation with States and local jurisdictions, enforcing national data standards for quality and consistency.\n**(4) Review of methodology by independent panel**\n**(A) Establishment**\nThe Secretary shall establish an independent advisory panel (in this paragraph referred to as the panel ) for the purposes of reviewing the methodology developed by the Secretary under subparagraph (C).\n**(B) Appointment of members**\nThe Comptroller General of the United States shall develop, maintain, and make publicly available a list of nominees to serve as members of the panel. The Secretary shall appoint a member of the panel only after reviewing such list. Such members shall be experts in epidemiology, statistics, public health surveillance, and data privacy.\n**(C) Review authority**\nThe Secretary shall develop and implement a methodology for the aggregation of health data for the purposes of the Repository, which shall go into effect only upon certification by the panel that such methodology\u2014\n**(i)**\nreflects scientific best practices; and\n**(ii)**\nmaintains public accessibility, privacy protections, and data comparability across jurisdictions.\n##### (i) Definitions\nIn this section:\n**(1) Health disparity**\nThe term health disparity means a difference in health outcomes or access to health services that is closely linked to social, economic, environmental, racial, ethnic, or other demographic factors.\n**(2) Local jurisdiction**\nThe term local jurisdiction means a municipality, county, local health department, or regional public health authority with the capacity to implement a neighborhood-level, publicly accessible health data platform.\n**(3) Medically underserved community**\nThe term medically underserved community has the meaning given such term in section 799B of the Public Health Service Act ( 42 U.S.C. 295p ).\n**(4) National Neighborhood Health Data Repository**\nThe term National Neighborhood Health Data Repository means the National Neighborhood Health Data Repository established under subsection (h).\n**(5) Neighborhood-level**\nThe term neighborhood-level means, with respect to a publicly accessible health data platform, that such health data platform focuses on a geographic area within a local jurisdiction that is smaller than the municipal or county level, such as a ZIP code, census tract, or community district.\n**(6) Publicly accessible health data platform**\nThe term publicly accessible health data platform means an online tool, website, or dashboard that makes health data accessible to the general public through visualizations, downloadable datasets, or written summaries.\n##### (j) Rule of construction\nNothing in this section shall be construed to preempt or supersede any applicable Federal, State, or local privacy laws.\n##### (k) Termination\nThe Program shall terminate on the date that is 4 years after the date on which the Secretary establishes the Program.",
      "versionDate": "2026-02-25",
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
        "name": "Health",
        "updateDate": "2026-03-27T20:08:14Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7717ih.xml"
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
      "title": "Community Health Profiles Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Health Profiles Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a pilot program at the Centers for Disease Control and Prevention to support local jurisdictions in developing neighborhood-level, publicly accessible health data platforms, to establish a National Neighborhood Health Data Repository, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T03:48:20Z"
    }
  ]
}
```

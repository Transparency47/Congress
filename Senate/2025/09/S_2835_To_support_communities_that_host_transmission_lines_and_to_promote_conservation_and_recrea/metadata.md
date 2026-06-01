# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2835?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2835
- Title: Energizing Our Communities Act
- Congress: 119
- Bill type: S
- Bill number: 2835
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2835",
    "number": "2835",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Energizing Our Communities Act",
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
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T17:40:27Z",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2835is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2835\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Welch (for himself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo support communities that host transmission lines and to promote conservation and recreation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Energizing Our Communities Act .\n#### 2. Community Economic Development Transmission Fund\n##### (a) Definitions\nIn this section:\n**(1) Covered loan**\nThe term covered loan means any of the following issued after the date of enactment of this Act:\n**(A)**\nA loan issued under section 40106(e)(1)(B) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18713(e)(1)(B) ).\n**(B)**\nA loan made for an eligible project described in paragraph (2)(B) under the Transmission Infrastructure Program of the Western Area Power Administration.\n**(C)**\nAny other loan made under a Department of Energy loan program identified in the report required under subsection (f)(1) with respect to electric power transmission lines that are capable of transmitting 999 megawatts or more.\n**(2) Eligible project**\nThe term eligible project means\u2014\n**(A)**\nan eligible project (as defined in section 40106(a) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18713(a) )) that is carried out using a covered loan described in paragraph (1)(A);\n**(B)**\na project for the purpose of constructing, financing, facilitating, planning, operating, or maintaining, or studying the construction of, new or upgraded electric power transmission lines and related facilities with at least 1 terminus within the service territory of the Western Area Power Administration that is carried out using a covered loan described in paragraph (1)(B); or\n**(C)**\na project with respect to electric power transmission lines capable of transmitting 999 megawatts or more that is carried out using a covered loan described in paragraph (1)(C).\n**(3) Fund**\nThe term Fund means the Community Economic Development Transmission Fund established under subsection (b).\n**(4) Host community**\nThe term host community means\u2014\n**(A)**\na local government, such as a municipality, town, or county, with jurisdiction over any land on which an eligible project is or will be carried out; or\n**(B)**\nan Indian Tribe with jurisdiction over any land on which an eligible project is or will be carried out.\n**(5) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(6) Secretary**\nThe term Secretary means the Secretary of Energy.\n##### (b) Establishment\nThere is established in the Treasury a fund, to be known as the Community Economic Development Transmission Fund \u2014\n**(1)**\nconsisting of such amounts as may be deposited in the Fund pursuant to subsection (c); and\n**(2)**\nthat shall be managed and administered by the Secretary to make payments, in accordance with this section, to host communities.\n##### (c) Deposits in the Fund\n**(1) In general**\nNotwithstanding any other provision of law, a portion, determined in accordance with paragraph (2), of the interest charged and collected with respect to a covered loan each fiscal year shall be deposited in the Fund to carry out the provisions of this Act.\n**(2) Determination of portion**\nThe Secretary, in consultation with the Secretary of the Treasury, shall determine the portion of interest charged and collected each fiscal year that shall be deposited in the Fund under this subsection.\n##### (d) Expenditures from the Fund\n**(1) Availability of amounts**\nAmounts in the Fund shall be available, as provided in appropriation Acts, for making payments as described in subsection (b)(2).\n**(2) Payments**\n**(A) In general**\nThe Secretary shall make a payment to a host community under this section not later than 18 months after construction of the applicable eligible project commences.\n**(B) Single sum**\nFor any 1 eligible project, the Secretary may make not more than 1 payment under this section to each host community eligible to receive a payment relating to that eligible project.\n**(3) Eligibility**\nA host community shall be eligible to receive a payment under this section if the host community\u2014\n**(A)**\nsubmits a request to the Secretary not later than 1 year after the host community receives notice under paragraph (4); and\n**(B)**\ncertifies to the Secretary that the funds will be used for an eligible purpose described in subsection (e).\n**(4) Notice**\nThe Secretary shall provide host communities notice of the availability of payments under this section as part of the Federal siting and permitting processes for the applicable eligible project.\n**(5) Payment amount**\nIn determining the amount of a payment to a host community under this section, the Secretary shall\u2014\n**(A)**\ndevelop and use a formula for disbursement of funds that, to the extent practicable, ensures the long-term solvency of the Fund; and\n**(B)**\nin developing that formula\u2014\n**(i)**\ntake into account input from host communities and stakeholder groups regarding the impacts of eligible projects on host communities; and\n**(ii)**\ninclude a small-population community minimum as part of the formula.\n**(6) Payments in lieu of taxes**\nAny amount received by a host community from a payment made under this section shall be in addition to any payment in lieu of taxes received by the host community under chapter 69 of title 31, United States Code.\n##### (e) Eligible use of funds\n**(1) Community support**\nA host community may use up to 80 percent of the amounts received by that host community from a payment under this section to develop, deliver, or support\u2014\n**(A)**\nservices, projects, or programs that\u2014\n**(i)**\nimprove existing infrastructure or implement essential public services, including services, projects, or programs relating to\u2014\n**(I)**\npublic schools;\n**(II)**\npublic libraries;\n**(III)**\npublic hospitals;\n**(IV)**\nroads, bridges, or public transportation;\n**(V)**\ncommunity centers or parks;\n**(VI)**\nfirefighting or search and rescue services; or\n**(VII)**\nlaw enforcement;\n**(ii)**\nprovide or expand access to\u2014\n**(I)**\nbroadband telecommunications services at local community anchor institutions (as defined in section 60302 of the Digital Equity Act of 2021 ( 47 U.S.C. 1721 ));\n**(II)**\ntechnology or connectivity needed for students to use a digital learning tool at or outside of a local school campus; or\n**(III)**\nfarmers markets or other agricultural support;\n**(iii)**\nsupport local agricultural processing or distribution infrastructure;\n**(iv)**\nsupport workforce training programs for technical training, skill mastery, or business opportunities across the spectrum of careers in renewable energy, with emphasis on historically underrepresented communities in the renewable energy workforce; or\n**(v)**\naddress public health by increasing outdoor recreation opportunities, including construction of new parks, for people of all backgrounds and abilities; or\n**(B)**\nother, similar services, projects, or programs.\n**(2) Conservation, stewardship, and recreation**\nA host community shall use at least 20 percent of the amounts received by that host community from a payment under this section for conservation, stewardship, or recreation purposes, including\u2014\n**(A)**\nrestoring or protecting\u2014\n**(i)**\nfish or wildlife habitat;\n**(ii)**\nfish or wildlife corridors; or\n**(iii)**\nwetlands, streams, rivers, or other natural water bodies in areas affected by transmission development;\n**(B)**\npreserving or improving recreational access to public land or water through an easement, right-of-way, or other instrument from willing landowners for the purpose of enhancing public access to existing Federal land or water that is inaccessible or restricted;\n**(C)**\ndeveloping new or renovating existing outdoor recreation facilities that provide outdoor recreation opportunities to the public;\n**(D)**\ncreating or significantly enhancing access to park or recreational opportunities in a neighborhood or community;\n**(E)**\nengaging or empowering underserved communities or youth;\n**(F)**\nfacilitating public-private partnerships to enhance public outdoor recreational access, infrastructure improvements, or conservation efforts;\n**(G)**\nfor natural climate solutions, including programs that\u2014\n**(i)**\naccommodate biochar or other nature-based opportunities for carbon sequestration;\n**(ii)**\nsupport wildfire resilience to ensure healthy and resilient forests or grasslands;\n**(iii)**\npromote the planting, growing, or restoring of trees or forests;\n**(iv)**\nsupport resilience against natural disasters to ensure healthy and resilient communities;\n**(v)**\nempower farmers in the United States to incorporate conservation or climate co-benefits in their agricultural practices; or\n**(vi)**\nsupport or implement traditional ecological knowledge; or\n**(H)**\nother, similar services, projects, or programs.\n##### (f) Reports\n**(1) Coverage**\nNot later than 90 days after the date of enactment of this Act, the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Energy and Commerce of the House of Representatives a report detailing the loan programs within the Department of Energy that fund electric power transmission lines and related infrastructure that are capable of transmitting 999 megawatts or more.\n**(2) Annual report**\n**(A) In general**\nNot later than 60 days after the end of each fiscal year, the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Energy and Commerce of the House of Representatives a report on the operation of the Fund during that fiscal year.\n**(B) Report requirements**\nEach report submitted under subparagraph (A) shall include\u2014\n**(i)**\na statement of\u2014\n**(I)**\nthe amounts deposited in the Fund during the applicable fiscal year; and\n**(II)**\nthe balance remaining in the Fund at the end of that fiscal year; and\n**(ii)**\na list of\u2014\n**(I)**\nhost communities that received amounts made available from the Fund during that fiscal year;\n**(II)**\nthe associated eligible projects carried out in those host communities; and\n**(III)**\nthe amount that each of those host communities received.\n##### (g) Savings provision\nNothing in this section, including the receipt of amounts made available from the Fund\u2014\n**(1)**\nprecludes a host community from entering into a community benefit agreement with an owner of transmission infrastructure; or\n**(2)**\notherwise affects the authority of a host community or an owner of transmission infrastructure with respect to any community benefit agreement.",
      "versionDate": "2025-09-17",
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
        "actionDate": "2025-09-17",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "5424",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Energizing Our Communities Act",
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
        "name": "Energy",
        "updateDate": "2025-11-17T18:40:20Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2835is.xml"
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
      "title": "Energizing Our Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T06:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Energizing Our Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to support communities that host transmission lines and to promote conservation and recreation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T06:03:29Z"
    }
  ]
}
```

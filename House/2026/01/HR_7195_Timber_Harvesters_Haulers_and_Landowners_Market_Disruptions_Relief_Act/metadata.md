# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7195?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7195
- Title: Timber Harvesters, Haulers, and Landowners Market Disruptions Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 7195
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-05-22T08:08:36Z
- Update date including text: 2026-05-22T08:08:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7195",
    "number": "7195",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "A000372",
        "district": "12",
        "firstName": "Rick",
        "fullName": "Rep. Allen, Rick W. [R-GA-12]",
        "lastName": "Allen",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Timber Harvesters, Haulers, and Landowners Market Disruptions Relief Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:36Z",
    "updateDateIncludingText": "2026-05-22T08:08:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:43:00Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7195ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7195\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mr. Allen introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo provide financial assistance to forest product harvesting and hauling businesses impacted by a significant market disruption, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Timber Harvesters, Haulers, and Landowners Market Disruptions Relief Act .\n#### 2. Financial assistance to forest harvesting and hauling businesses\n##### (a) In general\nIf the Secretary declares a market disruption under subsection (b), from amounts appropriated in subsection (f), the Secretary shall provide financial assistance payments to eligible entities in accordance with subsection (c).\n##### (b) Process for declaration of a market disruption\n**(1) In general**\nThe Governor of a State or the Chief of the Forest Service may petition the Secretary to declare a market disruption under paragraph (2).\n**(2) Declaration of a market disruption**\nNot later than 14 days after receiving a petition under paragraph (1), the Secretary shall\u2014\n**(A)**\ndeclare a market disruption; or\n**(B)**\nif the Secretary determines such market disruption relating to the petition does not exist, notify the petitioner with an explanation for such determination.\n##### (c) Payments to eligible entities\n**(1) Solicitation**\nNot later than 30 days after declaring a market disruption, the Secretary shall publish on the website of the United States Department of Agriculture or in the Federal Register a notice of funding availability under this section relating to such market disruption.\n**(2) Applications**\n**(A) Application date**\nNot later than 30 days after the publication of a notice of funding availability under paragraph (1), an eligible entity may apply for financial assistance by submitting the application described in subsection (d)(3) to the Secretary.\n**(B) Review**\nNot later than 30 days after receiving an application under subparagraph (A), the Secretary shall approve the application, deny the application, or request additional information from the applicant.\n**(3) Payments**\n**(A) Initial payment**\nNot later than 14 days after approving an application under paragraph (2), from amounts appropriated in subsection (f), the Secretary shall provide a payment, to be determined by the Secretary, of not more than $20,000 to the applicant.\n**(B) Second payment**\nOn September 30 following the date of the payment made under subparagraph (A), the Secretary may provide to an applicant that received funds under subparagraph (A) a payment of the difference between\u2014\n**(i)**\nthe payment made to the applicant under subparagraph (A); and\n**(ii)**\n30 percent of\u2014\n**(I)**\nthe estimated gross revenue of the eligible entity for the calendar year of such market disruption; minus\n**(II)**\nthe gross revenue of the eligible entity for the preceding calendar year.\n**(C) Subsequent payments**\n**(i) Request for continuing payment**\nIn each of the 5 years following the declaration of a market disruption, the Governor of a State or the Chief of the Forest Service that petitioned for the declaration of such market disruption under subsection (b)(1) may request the Secretary to continue providing payments under this section.\n**(ii) Determination**\nUpon receiving a request described in clause (i), the Secretary shall\u2014\n**(I)**\ndetermine whether the market conditions described in the applicable petition under subsection (b)(1) have improved; and\n**(II)**\nif such market conditions have not improved, pay an eligible entity an amount equal to 50 percent of the sum of payments under subparagraphs (A) and (B) previously made to such eligible entity.\n**(4) Proration**\nTo the extent that amounts appropriated under subsection (f) to carry out subparagraphs (B) and (C) of paragraph (3) are insufficient, the Secretary shall prorate amounts provided under such subparagraphs.\n**(5) Allowable uses**\nAn eligible entity that receives a payment under this section may only use the funds from such payment for\u2014\n**(A)**\nan operational expense (which may include payroll, fuel, equipment repairs, and debt service related to forest product harvesting or hauling); or\n**(B)**\nexpanding access to another market opportunity in the forest product sector.\n##### (d) Procedures\n**(1) Appeals**\n**(A) Submission**\nNot later than 30 days after the Secretary denies an application for payment under subsection (c)(2)(B), an applicant may submit an appeal to the National Appeals Division of the Department of Agriculture.\n**(B) Decision**\nNot later than 30 days after receiving an appeal under subparagraph (A), the National Appeals Division of the Department of Agriculture shall issue a decision on such appeal.\n**(2) False claims**\nAn entity that submits fraudulent information in any application under this section\u2014\n**(A)**\nmay not receive any funds under this section; and\n**(B)**\nshall be subject to fines, as determined to be appropriate by the Secretary.\n**(3) Development of application**\nNot later than 60 days after the date of the enactment of this section, the Secretary shall\u2014\n**(A)**\nestablish an application for purposes of applying for payments under this section; and\n**(B)**\ndevelop such application without regard to\u2014\n**(i)**\nthe notice and comment provisions of section 553 of title 5, United States Code; and\n**(ii)**\nchapter 35 of title 44, United States Code (commonly known as the Paperwork Reduction Act ).\n##### (e) Report\nFor each year in which the Secretary makes a payment under this section, the Secretary shall submit a report to Congress that summarizes each payment made and each activity carried out under this section during such year.\n##### (f) Appropriation\nThere is appropriated to carry out this section for each fiscal year an amount equal to the total amount collected in anti-dumping and countervailing duties on articles the Secretary determines are softwood lumber articles imported into the United States from Canada during that fiscal year.\n##### (g) Definitions\nIn this section:\n**(1)**\nThe term eligible entity means a forest product harvesting business (including a landowner that profits from timber grown on such land) or a forest product hauling business, that\u2014\n**(A)**\nhas suffered revenue loss related to a market disruption;\n**(B)**\nhas, in the calendar year preceding such market disruption, earned at least $35,000 in Federal taxable income by selling, harvesting, or hauling an unrefined forest product;\n**(C)**\nderives not less than 75 percent of its gross revenue from\u2014\n**(i)**\nforest product harvesting; or\n**(ii)**\nforest product hauling activity; and\n**(D)**\nin the case of a landowner that profits from timber grown on such land, has in at least 4 of the 5 previous calendar years sold not less than\u2014\n**(i)**\n1,000,000 board feet of sawtimber;\n**(ii)**\n2,000 cords of pulpwood; or\n**(iii)**\n5,000 green tons of any form of timber.\n**(2)**\nThe term gross revenue means the gross revenue generated by an eligible entity from forest product harvesting or forest product hauling service, within the normal range of operation of an eligible entity, as determined by the Secretary.\n**(3)**\nThe term region means a\u2014\n**(A)**\nState; or\n**(B)**\none of two portions of a State, as delineated by the Governor of that State or the Chief of the Forest Service.\n**(4)**\nThe term Secretary means the Secretary of Agriculture, acting through the Administrator of the Farm Services Agency.\n**(5)**\nThe term market disruption means\u2014\n**(A)**\nthe closure or idling, during the 5 years preceding the date of the petition under subsection (b), of one or more processing facility for a particular forest product, including a pulp mill that process pine pulpwood, that represents a loss of at least 20 percent processing capacity for that forest product within a region;\n**(B)**\na trade barrier imposed by a foreign entity that results in a national reduction of at least 50 percent in export receipts for a particular forest product, including hardwood lumber and Douglas-fir sawlogs, as compared to the export receipts from the year preceding the date of the petition under subsection (b);\n**(C)**\na decrease, during the 2 years preceding the date of the petition under subsection (b), of at least 50 percent of the average stumpage price or delivered price of a particular forest product in a region;\n**(D)**\nat least 20 percent of a region by area has, during the 10 years preceding the date of the petition under subsection (b), lost access to previously existing markets for a particular forest product; or\n**(E)**\nan event that poses a significant threat to the viability of timber harvesting and hauling operations in the United States.",
      "versionDate": "2026-01-22",
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
        "updateDate": "2026-01-23T14:31:52Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7195ih.xml"
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
      "title": "Timber Harvesters, Haulers, and Landowners Market Disruptions Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-23T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Timber Harvesters, Haulers, and Landowners Market Disruptions Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-23T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide financial assistance to forest product harvesting and hauling businesses impacted by a significant market disruption, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-23T09:18:22Z"
    }
  ]
}
```

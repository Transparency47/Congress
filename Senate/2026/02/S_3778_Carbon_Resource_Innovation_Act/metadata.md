# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3778?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3778
- Title: Carbon Resource Innovation Act
- Congress: 119
- Bill type: S
- Bill number: 3778
- Origin chamber: Senate
- Introduced date: 2026-02-04
- Update date: 2026-03-20T11:03:19Z
- Update date including text: 2026-03-20T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in Senate
- 2026-02-04 - IntroReferral: Introduced in Senate
- 2026-02-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-04: Introduced in Senate

## Actions

- 2026-02-04 - IntroReferral: Introduced in Senate
- 2026-02-04 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3778",
    "number": "3778",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Carbon Resource Innovation Act",
    "type": "S",
    "updateDate": "2026-03-20T11:03:19Z",
    "updateDateIncludingText": "2026-03-20T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T19:10:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "WA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3778is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3778\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2026 Mr. Sheehy (for himself and Ms. Cantwell ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the carbon oxide sequestration credit to include solid or liquid carbon capture facilities.\n#### 1. Short title\nThis Act may be cited as the Carbon Resource Innovation Act .\n#### 2. Expansion of carbon oxide sequestration credit to include solid or liquid carbon capture facilities\n##### (a) In general\nSection 45Q of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (B)(iii), by striking or at the end,\n**(B)**\nin subparagraph (C)(ii), by striking the period at the end and inserting , or , and\n**(C)**\nby adding at the end the following new subparagraph:\n(D) in the case of a solid or liquid carbon capture facility, any carbon which\u2014 (i) is captured in liquid or solid form by carbon capture equipment, (ii) if not captured, would be expected to\u2014 (I) be released into the atmosphere by natural processes as an emission of greenhouse gas, or (II) lead to such release through a comparison system (as such term is used in Treasury Regulation section 1.45Q\u20134(c)(2)), and (iii) is measured at the source of capture and verified at the point of disposal, injection, or utilization. ,\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking or direct air capture facility and inserting , direct air capture facility, or solid or liquid carbon capture facility , and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (B)(ii), by striking or at the end,\n**(ii)**\nby redesignating subparagraph (C) as subparagraph (D), and\n**(iii)**\nby inserting after subparagraph (B) the following new subparagraph:\n(C) in the case of a solid or liquid carbon capture facility, captures not less than 1,000 metric tons of qualified carbon oxide during the taxable year, or ,\n**(3)**\nin subsection (e)\u2014\n**(A)**\nby redesignating paragraph (5) as paragraph (6), and\n**(B)**\nby inserting after paragraph (4) the following new paragraph:\n(5) Solid or liquid carbon capture facility (A) In general The term solid or liquid carbon capture facility means any facility which uses carbon capture equipment to capture carbon in solid or liquid form that would otherwise be released into the atmosphere as a carbon oxide, including a facility which results in a net reduction of carbon when compared to a comparison system (as described in Treasury Regulation section 1.45Q\u20134(c)(2)). (B) Other terms With respect to a facility described in subparagraph (A)\u2014 (i) the term capture means, with respect to carbon, the process which enables disposal, injection, or utilization of such carbon, and (ii) the term carbon capture equipment means any equipment used at such facility. , and\n**(4)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (2), by inserting , and in the case of solid or liquid carbon capture facilities, shall also include underground storage chambers under such conditions that the carbon does not escape into the atmosphere after under such regulations , and\n**(B)**\nby adding at the end the following new paragraph:\n(11) Carbon captured by solid or liquid carbon capture facility For purposes of this section, the amount of carbon which is captured by the taxpayer at a solid or liquid carbon capture facility shall be equal to the carbon dioxide equivalent of the metric tons of carbon which are measured at the source of capture and verified at the point of disposal, injection, or utilization. .\n##### (b) Effective date\nThe amendments made by this section shall apply to carbon captured after the date of enactment of this Act.",
      "versionDate": "2026-02-04",
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
        "name": "Taxation",
        "updateDate": "2026-02-23T22:15:27Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3778is.xml"
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
      "title": "Carbon Resource Innovation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Carbon Resource Innovation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to expand the carbon oxide sequestration credit to include solid or liquid carbon capture facilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:34Z"
    }
  ]
}
```

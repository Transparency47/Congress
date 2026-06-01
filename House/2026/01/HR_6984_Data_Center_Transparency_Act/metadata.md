# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6984?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6984
- Title: Data Center Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 6984
- Origin chamber: House
- Introduced date: 2026-01-08
- Update date: 2026-05-27T08:06:03Z
- Update date including text: 2026-05-27T08:06:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-08: Introduced in House

## Actions

- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6984",
    "number": "6984",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001226",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Menendez, Robert [D-NJ-8]",
        "lastName": "Menendez",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Data Center Transparency Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:03Z",
    "updateDateIncludingText": "2026-05-27T08:06:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-08",
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
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T15:02:30Z",
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
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "PA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "IN"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MN"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "KS"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6984ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6984\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 8, 2026 Mr. Menendez (for himself and Mr. Casar ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require reports on the effects of data centers on air quality and water quality, and on electricity consumption by data centers.\n#### 1. Short title\nThis Act may be cited as the Data Center Transparency Act .\n#### 2. Reports on the effects of data centers on air quality and water quality; reports on electricity consumption by data centers\n##### (a) Reports on the effects of data centers on air quality and water quality\nNot later than 6 months after the date of enactment of this section, and not less frequently than once every 3 months thereafter, the Administrator of the Environmental Protection Agency shall submit to Congress, and make publicly available on a website, a report that identifies, with respect to the period of 3 months preceding the submission and publication of the report\u2014\n**(1)**\nthe total amount of water consumed by data centers located in the United States;\n**(2)**\nhow such data centers reuse water, and the amount of such reused water;\n**(3)**\nhow such data centers affect local water systems, including with respect to\u2014\n**(A)**\nthe availability of potable water;\n**(B)**\nwhether the data center increased demand on local water utilities;\n**(C)**\nany potential data on service disruptions for other customers of local water utilities;\n**(D)**\nany changes in residential rates for water services; and\n**(E)**\nthe type and amount of pollutants (as such term is defined in section 502(6) of the Federal Water Pollution Control Act ( 33 U.S.C. 1362(6) )) discharged into water by data centers;\n**(4)**\nthe total amount of greenhouse gases emitted from such data centers; and\n**(5)**\nthe effect of such greenhouse gas emissions, including the cumulative effect on overburdened communities.\n##### (b) Reports on electricity consumption by data centers\n**(1) Collection of data**\nThe Administrator of the Energy Information Administration shall collect data on the total amount of energy consumed every 6 months by each data center located in the United States.\n**(2) Reports**\nNot later than 6 months after the date of enactment of this section, and not less frequently than once every 6 months thereafter, the Administrator of the Energy Information Administration shall submit to Congress, and make publicly available on a website, a report that identifies, with respect to the period of 6 months preceding the submission and publication of the report\u2014\n**(A)**\nthe total amount of energy consumption by data centers, disaggregated by State;\n**(B)**\nhow such energy consumption may have changed during such period of 6 months;\n**(C)**\nthe number of data centers that began operating during such period of 6 months;\n**(D)**\nhow household energy bills may have changed during such period of 6 months; and\n**(E)**\nthe average household energy use and cost.\n##### (c) Data center defined\nIn this section, the term data center has the meaning given such term in section 453(a) of the Energy Independence and Security Act of 2007 ( 42 U.S.C. 17112(a) ).",
      "versionDate": "2026-01-08",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-26T14:41:27Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6984ih.xml"
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
      "title": "Data Center Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T07:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Data Center Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require reports on the effects of data centers on air quality and water quality, and on electricity consumption by data centers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T05:33:36Z"
    }
  ]
}
```

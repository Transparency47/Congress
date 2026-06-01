# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1638?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1638
- Title: Protection Against Foreign Adversarial Artificial Intelligence Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1638
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-08-01T11:03:20Z
- Update date including text: 2025-08-01T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1638",
    "number": "1638",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Protection Against Foreign Adversarial Artificial Intelligence Act of 2025",
    "type": "S",
    "updateDate": "2025-08-01T11:03:20Z",
    "updateDateIncludingText": "2025-08-01T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T19:29:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NV"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "HI"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1638is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1638\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Cassidy (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo protect the United States from artificial intelligence applications based in or affiliated with countries of concern, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protection Against Foreign Adversarial Artificial Intelligence Act of 2025 .\n#### 2. Prohibition on use of DeepSeek to carry out a Federal contract\n##### (a) Prohibition\nExcept as provided in subsection (b), no Federal contractor with an active Federal contract may use the DeepSeek application or any successor application or service developed or provided by High Flyer or any entity owned by High Flyer, for the fulfillment, assistance, execution, or otherwise support to complete, or support in part, a contract with a Federal agency.\n##### (b) Waiver\nThe Secretary of Commerce may, in consultation with the Secretary of Defense, waive the prohibition in subsection (a) on a case-by-case basis if using the application or service is required for the completion of a national security-related objective of a certain contract or for research purposes.\n#### 3. Report on threats to national security posed by artificial intelligence platforms based in or affiliated with countries of concern\n##### (a) Definition of country of concern\nIn this section, the term country of concern has the meaning given the term covered nation in section 4872(f) of title 10, United States Code.\n##### (b) Report required\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Commerce shall, in consultation with the Secretary of Defense, submit to the Committee on Armed Services of the Senate and of the House of Representatives, the Committee on Commerce, Science, and Transportation of the Senate, and the Committee on Energy and Commerce of the House of Representatives a detailed report on the threats to national security posed by artificial intelligence platforms, including large language models and generative artificial intelligence, based in or affiliated with countries of concern.\n##### (c) Contents\nThe report submitted pursuant to subsection (b) shall include the following:\n**(1)**\nAn analysis of censorship laws and capacities by governments described in subsection (a) that could access or influence of artificial intelligence applications.\n**(2)**\nAn analysis of the potential and current use of artificial intelligence platforms to further state-sponsored propaganda.\n**(3)**\nThe national security impact of circumvention of United States export controls on graphics processing units contributed to the development of artificial intelligence models of countries of concern.\n**(4)**\nAn analysis of the privacy and data security threats toward United States data entered or otherwise submitted to an artificial intelligence application, including\u2014\n**(A)**\nhow and where United States users\u2019 data is stored, including whether such data is stored within on-premise servers or a cloud infrastructure;\n**(B)**\nwhether United States users\u2019 data can be accessed and used by a government or political entity of a country of concern, including the Chinese Communist Party;\n**(C)**\nthe extent to which data collected from the United States contributes to the development of artificial intelligence applications described in subsection (b);\n**(D)**\nthe threat that such access could be an economic espionage risk to intellectual property, trade secrets, proprietary information, or sensitive or confidential information to obtain an unlawful advantage; and\n**(E)**\nthe threat that such access could be a risk to information, including policy decisions, relating to an office or program under the Federal Government.\n**(5)**\nAny other information considered relevant by the Secretary.\n**(6)**\nRecommendations for administrative and legislative action to address data security and privacy risks posed to the United States by artificial intelligence applications affiliated with governments of countries of concern.\n##### (d) Form\nThe report submitted pursuant to subsection (b) shall be submitted in unclassified form, but may include a classified annex.",
      "versionDate": "2025-05-07",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-27T14:04:12Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1638is.xml"
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
      "title": "Protection Against Foreign Adversarial Artificial Intelligence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protection Against Foreign Adversarial Artificial Intelligence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect the United States from artificial intelligence applications based in or affiliated with countries of concern, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:31Z"
    }
  ]
}
```

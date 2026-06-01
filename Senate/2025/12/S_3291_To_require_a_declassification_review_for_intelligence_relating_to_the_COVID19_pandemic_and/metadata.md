# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3291?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3291
- Title: Enhanced COVID-19 Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3291
- Origin chamber: Senate
- Introduced date: 2025-12-01
- Update date: 2026-04-16T18:06:36Z
- Update date including text: 2026-04-16T18:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in Senate
- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.
- Latest action: 2025-12-01: Introduced in Senate

## Actions

- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3291",
    "number": "3291",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Enhanced COVID-19 Transparency Act of 2025",
    "type": "S",
    "updateDate": "2026-04-16T18:06:36Z",
    "updateDateIncludingText": "2026-04-16T18:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Intelligence (Select) Committee",
          "systemCode": "slin00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Select Committee on Intelligence.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T23:30:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Intelligence (Select) Committee",
      "systemCode": "slin00",
      "type": "Select"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3291is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3291\nIN THE SENATE OF THE UNITED STATES\nDecember 1, 2025 Mr. Young introduced the following bill; which was read twice and referred to the Select Committee on Intelligence\nA BILL\nTo require a declassification review for intelligence relating to the COVID\u201319 pandemic, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhanced COVID-19 Transparency Act of 2025 .\n#### 2. Declassification of intelligence and additional transparency measures relating to the COVID\u201319 pandemic\n##### (a) Definitions\nIn this section, the terms congressional intelligence committees and intelligence community have the meanings given such terms in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 ).\n##### (b) In general\nNot later than 180 days after the date of the enactment of this Act, the Director of National Intelligence and each head of an element of the intelligence community shall jointly\u2014\n**(1)**\nperform a declassification review of intelligence products relating to the origins of the Coronavirus Disease 2019 (COVID\u201319), including\u2014\n**(A)**\nresearch conducted at the Wuhan Institute of Virology or any other medical or scientific research center within the People\u2019s Republic of China;\n**(B)**\ninformation relating to Gain of Function research and the intention of this research; and\n**(C)**\ninformation relating to sources of funding or direction for research on coronaviruses, including both sources within the People\u2019s Republic of China and foreign sources;\n**(2)**\nperform a declassification review of intelligence products relating to efforts by government officials of entities of the People\u2019s Republic of China\u2014\n**(A)**\nto disrupt or obstruct information sharing or investigations into the origins of the coronavirus disease 2019 (COVID\u201319) pandemic;\n**(B)**\nto disrupt the sharing of medically significant information relating to the transmissibility and potential harm of SARS\u2013CoV\u20132 to humans, including\u2014\n**(i)**\nefforts to limit the sharing of information with the United States Government;\n**(ii)**\nefforts to limit the sharing of information with the governments of allies and partners of the United States; and\n**(iii)**\nefforts to limit the sharing of information with the United Nations and World Health Organization;\n**(C)**\nto obstruct or otherwise limit the sharing of information between national, provincial, and city governments within the People\u2019s Republic of China and between subnational entities within the People's Republic of China and external researchers;\n**(D)**\nto deny the sharing of information with the United States, allies and partners of the United States, or multilateral organizations, including the United Nations and the World Health Organization;\n**(E)**\nto pressure or lobby foreign governments, journalists, medical researchers, officials of the United States Government, or officials of multilateral organizations (including the United Nations and the World Health Organization) with respect to the source, scientific origins, transmissibility, or other attributes of the SARS\u2013CoV\u20132 virus or the COVID\u201319 pandemic;\n**(F)**\nto disrupt government or private-sector efforts to conduct research and development of medical interventions or countermeasures for the COVID\u201319 pandemic, including vaccines; and\n**(G)**\nto promote alternative narratives regarding the origins of COVID\u201319 as well as the domestic Chinese and international response to the COVID\u201319 pandemic;\n**(3)**\nmake available to the public appropriately declassified intelligence products described under paragraphs (1) and (2), including such redactions as the Director, with the concurrence of the head of the originating element of the intelligence community, determines necessary to protect sources and methods and information concerning United States persons; and\n**(4)**\nsubmit to the congressional intelligence committees an unredacted version of the declassified intelligence products described in paragraph (3).",
      "versionDate": "2025-12-01",
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-29",
        "text": "By Senator Cotton from Select Committee on Intelligence filed written report. Report No. 119-51. Minority views filed."
      },
      "number": "2342",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Intelligence Authorization Act for Fiscal Year 2026",
      "type": "S"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-08T16:26:01Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3291is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a declassification review for intelligence relating to the COVID-19 pandemic, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T07:58:42Z"
    },
    {
      "title": "Enhanced COVID-19 Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Enhanced COVID-19 Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:38:19Z"
    }
  ]
}
```

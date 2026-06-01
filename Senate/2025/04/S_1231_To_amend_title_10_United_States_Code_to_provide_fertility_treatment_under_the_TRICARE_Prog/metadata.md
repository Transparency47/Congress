# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1231?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1231
- Title: IVF for Military Families Act
- Congress: 119
- Bill type: S
- Bill number: 1231
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2025-12-05T21:58:10Z
- Update date including text: 2025-12-05T21:58:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1231",
    "number": "1231",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "IVF for Military Families Act",
    "type": "S",
    "updateDate": "2025-12-05T21:58:10Z",
    "updateDateIncludingText": "2025-12-05T21:58:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T19:51:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1231is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1231\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Ms. Duckworth (for herself and Mrs. Murray ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to provide fertility treatment under the TRICARE Program.\n#### 1. Short title\nThis Act may be cited as the IVF for Military Families Act .\n#### 2. Fertility treatment for certain members of the uniformed services and dependents\n##### (a) Fertility treatment\nChapter 55 of title 10, United States Code, is amended by inserting after section 1074o the following new section:\n1074p. Fertility treatment for certain active duty members of the uniformed services and their dependents (a) Coverage The Secretary of Defense shall ensure that fertility-related care for a member of the uniformed services on active duty (or a dependent of such a member) shall be covered under TRICARE Prime and TRICARE Select. (b) In vitro fertilization In the case of in vitro fertilization treatment furnished to an individual pursuant to subsection (a)\u2014 (1) not more than three completed oocyte retrievals may be furnished; and (2) unlimited embryo transfers may be provided in accordance with the guidelines of the American Society for Reproductive Medicine. (c) Definitions In this section: (1) The term infertility means a disease, condition, or status characterized by\u2014 (A) the failure to establish a pregnancy or to carry a pregnancy to live birth after regular, unprotected sexual intercourse in accordance with the guidelines of the American Society for Reproductive Medicine; (B) the inability of an individual to reproduce without medical intervention either as a single individual or with the partner of the individual; or (C) the findings of a licensed physician based on the medical, sexual, and reproductive history, age, physical findings, or diagnostic testing of the individual. (2) The term fertility-related care means\u2014 (A) the diagnosis of infertility; and (B) fertility treatment. (3) The term fertility treatment includes the following: (A) In vitro fertilization or other treatments or procedures in which human oocytes, embryos, or sperm are handled when clinically appropriate. (B) Sperm retrieval. (C) Egg retrieval. (D) Preservation of human oocytes, embryos, or sperm. (E) Artificial insemination, including intravaginal insemination, intracervical insemination, and intrauterine insemination. (F) Transfer of reproductive genetic material. (G) Medications as prescribed or necessary for fertility. (H) Fertility treatment coordination. (I) Such other information, referrals, treatments, procedures, testing, medications, laboratory services, technologies, and services facilitating reproduction as determined appropriate by the Secretary of Defense. .\n##### (b) Program on fertility treatment coordination\nChapter 55 of title 10, United States Code, is amended by adding at the end the following new section:\n1110c. Program on fertility-related care coordination (a) In general The Secretary of Defense shall establish a program on the coordination of fertility-related care by the Secretary for purposes of ensuring patients receive timely fertility-related care. (b) Training and support In carrying out the program established under subsection (a), the Secretary shall provide to community health care providers training and support with respect to the unique needs of members of the uniformed services and the dependents of such members. (c) Fertility-Related care defined In this section, the term fertility-related care has the meaning given that term in section 1074p(c) of this title. .\n##### (c) Conforming amendment\nSection 1079(a) of title 10, United States Code, is amended by adding at the end the following new paragraph:\n(21) Fertility-related care shall be provided in accordance with section 1074p of this title. .\n##### (d) Application\nThe amendments made by this section shall apply with respect to services provided on or after October 1, 2027.",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "2557",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "IVF for Military Families Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-22T00:42:58Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1231is.xml"
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
      "title": "IVF for Military Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "IVF for Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to provide fertility treatment under the TRICARE Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:59Z"
    }
  ]
}
```

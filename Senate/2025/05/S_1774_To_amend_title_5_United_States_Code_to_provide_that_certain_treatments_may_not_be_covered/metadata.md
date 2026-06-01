# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1774?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1774
- Title: Protecting Minors in Federal Health Plans Act
- Congress: 119
- Bill type: S
- Bill number: 1774
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2025-05-30T12:05:08Z
- Update date including text: 2025-05-30T12:05:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1774",
    "number": "1774",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Protecting Minors in Federal Health Plans Act",
    "type": "S",
    "updateDate": "2025-05-30T12:05:08Z",
    "updateDateIncludingText": "2025-05-30T12:05:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T15:50:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WY"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NE"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1774is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1774\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Risch (for himself, Ms. Lummis , Mr. Ricketts , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to provide that certain treatments may not be covered under the health insurance program carried out under chapter 89 of that title, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Minors in Federal Health Plans Act .\n#### 2. Prohibitions on FEHB coverage for certain treatment\n##### (a) In general\nSection 8902 of title 5, United States Code, is amended by adding at the end the following:\n(q) (1) In this subsection, the term gender-affirming care or service \u2014 (A) means a medical intervention designed to treat gender dysphoria; (B) includes hormone therapy, the use of puberty blockers, and any surgical procedure aimed at gender transition; and (C) notwithstanding subparagraphs (A) and (B), does not include\u2014 (i) a service provided to an individual with a medically verifiable disorder of sexual development, including an individual with an irresolvable and ambiguous external sex characteristic, including an individual born with\u2014 (I) 46 XY chromosomes and under-virilization; (II) 46 XX chromosomes and virilization; or (III) both ovarian and testicular tissue; (ii) a service provided to treat a disorder diagnosed by a physician in which the physician has determined through genetic or biochemical testing that the applicable individual has abnormal (or otherwise inconsistent with typical male or female characteristics)\u2014 (I) sex chromosome structure; (II) sex steroid hormone production; or (III) sex steroid hormone action; (iii) the treatment of any infection, injury, disease, or disorder that has been caused or worsened by a medical intervention described in subparagraph (A), without regard to whether that intervention\u2014 (I) was performed in compliance with State or Federal law; or (II) was covered under a contract under this chapter, as of the date on which the intervention was performed; (iv) any procedure that\u2014 (I) is performed to address a physical disorder, injury, or illness that, as certified by a physician, poses an imminent risk of death or impairment of major bodily function; and (II) is not performed for the purpose of gender transition or to alleviate psychological, physical, or mental distress relating to gender; (v) a prescription for puberty suppression or blocking that is used to normalize puberty in an individual younger than 18 years of age who has been diagnosed with precocious puberty; (vi) any hormone therapy procedure that is used to stimulate puberty in an individual younger than 18 years of age who has been diagnosed with delayed puberty, if the hormones administered through that procedure are\u2014 (I) consistent with the biological sex of the individual; and (II) used to stimulate a normal puberty consistent with the biological sex of the individual; or (vii) male circumcision. (2) Subject to paragraph (3), and notwithstanding any other provision of law or regulation, a contract under this chapter may not include coverage for any gender-affirming care or service for any individual younger than 18 years of age. (3) In the case of an individual who, as of the effective date of this subsection, is younger than 18 years of age and who, as of that effective date, is undergoing hormone therapy that, as of the day before that effective date, is covered by a contract under this chapter, that hormone therapy may continue to be covered under such a contract after that effective date if the hormone therapy is provided pursuant to a reduction schedule that\u2014 (A) is supervised by a physician; and (B) requires that therapy to conclude not later than 1 year after that effective date. .\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply with respect to any contract entered into, or renewed for a contract year, on or after the date of enactment of this Act.",
      "versionDate": "2025-05-15",
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
        "name": "Health",
        "updateDate": "2025-05-30T12:05:08Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1774is.xml"
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
      "title": "Protecting Minors in Federal Health Plans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Minors in Federal Health Plans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to provide that certain treatments may not be covered under the health insurance program carried out under chapter 89 of that title, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:21Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4172
- Title: AFTER Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4172
- Origin chamber: Senate
- Introduced date: 2026-03-24
- Update date: 2026-04-06T13:26:13Z
- Update date including text: 2026-04-06T13:26:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in Senate
- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S1581-1582)
- Latest action: 2026-03-24: Introduced in Senate

## Actions

- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S1581-1582)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4172",
    "number": "4172",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "AFTER Act of 2026",
    "type": "S",
    "updateDate": "2026-04-06T13:26:13Z",
    "updateDateIncludingText": "2026-04-06T13:26:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-24",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S1581-1582)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:55:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4172is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4172\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2026 Ms. Collins (for herself and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Animal Welfare Act to allow for the retirement of certain animals used in Federal research, and for other purposes.\n#### 1. Short Title\nThis Act may be cited as the Animal Freedom from Testing, Experiments, and Research Act of 2026 or the AFTER Act of 2026 .\n#### 2. Placement of animals used in Federal research\n##### (a) In general\nSection 14 of the Animal Welfare Act ( 7 U.S.C. 2144 ) is amended to read as follows:\n14. Standards for Federal facilities (a) Definitions In this section: (1) Animal rescue organization The term animal rescue organization means a nonprofit organization the purpose of which is to rescue covered animals and find permanent adoptive homes for those animals. (2) Animal sanctuary The term animal sanctuary means a nonprofit organization that\u2014 (A) is registered with the Secretary; (B) operates a place of refuge in which\u2014 (i) a covered animal is provided care for the lifetime of the animal; and (ii) an unescorted public visitation of that animal is not permitted; (C) does not engage in commercial trade of covered animals; (D) does not breed covered animals; (E) does not permit direct contact between the public and covered animals; (F) does not allow the use of a covered animal for performance or exhibition purposes; and (G) does not conduct or permit research on a covered animal other than noninvasive behavioral research. (3) Animal shelter The term animal shelter means a facility that\u2014 (A) accepts or seizes covered animals\u2014 (i) to care for the animals; (ii) to place those animals in a permanent adoptive home; or (iii) for purposes of law enforcement; and (B) does not\u2014 (i) engage in commercial trade of covered animals; (ii) breed covered animals; (iii) allow the use of a covered animal for performance or exhibition purposes; or (iv) conduct or permit research on a covered animal other than noninvasive behavioral research. (4) Covered animal (A) In general The term covered animal means an animal that is unwanted, abandoned, or otherwise in need of placement in a home. (B) Exclusions The term covered animal does not include\u2014 (i) a rat of the genus Rattus; or (ii) a mouse of the genus Mus. (5) Nonprofit organization The term nonprofit organization means an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of that Code. (6) Suitable for retirement The term suitable for retirement means, with respect to an animal, that the animal has been evaluated by a licensed veterinarian and is determined to be mentally and physically healthy. (b) Laboratory animal facilities and exhibitors Any department, agency, or instrumentality of the United States that operates laboratory animal facilities or exhibits animals shall comply with the standards and other requirements promulgated by the Secretary under subsections (a), (g), (h), and (i) of section 13. (c) Retirement (1) In general Not later than 90 days after the date of enactment of the AFTER Act of 2026 , any department, agency, or instrumentality of the United States operating a Federal research facility shall, after public notice and comment, promulgate regulations that, with respect to any animal of the facility that is no longer needed for research and determined to be suitable for retirement\u2014 (A) facilitate and encourage the adoption of the animal by, or placement of the animal with\u2014 (i) an animal rescue organization, animal sanctuary, animal shelter, or individual who intends to keep the animal as a pet; or (ii) in the case of a nonhuman primate, an animal sanctuary; and (B) to the maximum extent practicable, collaborate with appropriate nonprofit organizations to carry out subparagraph (A). (2) National placement The regulations promulgated to carry out paragraph (1)(A) shall include consideration of placing animals with the entities described in that subparagraph that are located beyond the immediate geographic vicinity of the Federal research facility at which the animal being retired is located. (d) Effect on other laws Nothing in this section, including regulations promulgated under subsection (c)(1), shall\u2014 (1) preempt any State or local law relating to the adoption or placement of animals used in research that is more stringent than the requirements of this section; (2) prohibit, prevent, forestall, or otherwise impede the placement of any chimpanzee that has been used, or was bred or purchased for use, in research conducted or supported by a Federal agency into the sanctuary system established under section 404K of the Public Health Service Act ( 42 U.S.C. 283m ); or (3) prevent a State or unit of local government from adopting or enforcing an animal welfare law that is more stringent than this section. .\n##### (b) Technical amendments\nSection 13 of the Animal Welfare Act ( 7 U.S.C. 2143 ) is amended\u2014\n**(1)**\nby redesignating subsections (g) and (h) as subsections (h) and (i), respectively; and\n**(2)**\nby redesignating the second subsection (f) (relating to the certification requirement for the delivery of any animal) as subsection (g).",
      "versionDate": "2026-03-24",
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
        "name": "Animals",
        "updateDate": "2026-04-06T13:26:13Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4172is.xml"
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
      "title": "AFTER Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AFTER Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Animal Freedom from Testing, Experiments, and Research Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Animal Welfare Act to allow for the retirement of certain animals used in Federal research, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:26Z"
    }
  ]
}
```

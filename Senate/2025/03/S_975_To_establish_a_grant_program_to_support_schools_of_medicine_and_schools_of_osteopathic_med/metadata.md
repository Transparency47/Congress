# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/975?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/975
- Title: Expanding Medical Education Act
- Congress: 119
- Bill type: S
- Bill number: 975
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-12-05T21:44:30Z
- Update date including text: 2025-12-05T21:44:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/975",
    "number": "975",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Expanding Medical Education Act",
    "type": "S",
    "updateDate": "2025-12-05T21:44:30Z",
    "updateDateIncludingText": "2025-12-05T21:44:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T17:07:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s975is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 975\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Kaine (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish a grant program to support schools of medicine and schools of osteopathic medicine in underserved areas.\n#### 1. Short title\nThis Act may be cited as the Expanding Medical Education Act .\n#### 2. Grants for schools of medicine and schools of osteopathic medicine in underserved areas\nSubpart II of part C of title VII of the Public Health Service Act ( 42 U.S.C. 293m et seq. ) is amended by adding at the end the following:\n749C. Grants for schools of medicine and schools of osteopathic medicine in underserved areas (a) In general The Secretary may award grants to institutions of higher education (including consortiums of such institutions) for the establishment, improvement, or expansion of a school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine. (b) Priority In selecting grant recipients under this section, the Secretary shall give priority to any institution of higher education (or consortium of such institutions) that\u2014 (1) proposes to use the grant for the establishment of a school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine, in an area\u2014 (A) in which\u2014 (i) no other such school is based; or (ii) in the case in which the school of medicine or osteopathic medicine proposed to be established would be a minority-serving institution, no other minority-serving institution that includes a school of medicine or osteopathic medicine is based; and (B) that is a medically underserved community or a health professional shortage area; or (2) is a minority-serving institution described in section 371(a) of the Higher Education Act of 1965 or an institution or program described in section 326(e) of such Act. (c) Considerations In awarding grants under this section, the Secretary, to the extent practicable, may ensure equitable distribution of awards among the geographical regions of the United States. (d) Use of funds An institution of higher education (or a consortium of such institutions)\u2014 (1) shall use grant amounts received under this section to\u2014 (A) recruit, enroll, and retain medical students who are pursuing a degree of doctor of medicine or doctor of osteopathy, including individuals who are from disadvantaged backgrounds (including racial and ethnic groups underrepresented among medical students and health professions), individuals from rural and underserved areas, low-income individuals, and first generation college students, at a school of medicine or osteopathic medicine or branch campus of a school of medicine or osteopathic medicine; and (B) develop, implement, and expand curriculum that emphasizes care for rural and underserved populations, including accessible and culturally and linguistically appropriate care and services, at such school or branch campus; and (2) may use grant amounts received under this section to\u2014 (A) plan and construct\u2014 (i) a school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine, in an area in which no other such school is based; or (ii) a school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine, that will be a minority-serving institution, in an area in which no other such school that is a minority-serving institution is based; (B) plan, develop, and meet criteria for accreditation for a school of medicine or osteopathic medicine or branch campus of a school of medicine or osteopathic medicine; (C) hire faculty, including faculty from racial and ethnic groups who are underrepresented among the medical and other health professions, and other staff to serve at such a school or branch campus; (D) support educational programs at such a school or branch campus; (E) modernize and expand infrastructure at such a school or branch campus; and (F) support other activities that the Secretary determines further the establishment, improvement, or expansion of a school of medicine or osteopathic medicine or branch campus of a school of medicine or osteopathic medicine. (e) Application To be eligible to receive a grant under subsection (a), an institution of higher education (or a consortium of such institutions), shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including a description of the institution\u2019s or consortium's planned activities described in subsection (d). (f) Reporting (1) Reports from entities Each institution of higher education, or consortium of such institutions, awarded a grant under this section shall submit an annual report to the Secretary on the activities conducted under such grant, and other information as the Secretary may require. (2) Report to Congress Not later than 5 years after the date of enactment of this section and every 5 years thereafter, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that provides a summary of the activities and outcomes associated with grants made under this section. Such reports shall include\u2014 (A) a list of awardees, including their primary geographic location, and location of any school of medicine or osteopathic medicine, or a branch campus of school of medicine or osteopathic medicine that was established, improved, or expanded under this program; (B) the total number of students (including the number of students from racial and ethnic groups underrepresented among medical students and health professions, low-income students, and first generation college students) who\u2014 (i) are enrolled at or who have graduated from any school of medicine or osteopathic medicine, or a branch campus of school of medicine or osteopathic medicine, that was established, improved, or expanded under this program, deidentified and disaggregated by race, ethnicity, age, sex, geographic region, disability status, and other relevant factors, to the extent such information is available; and (ii) who subsequently participate in an accredited internship or medical residency program upon graduation from any school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine, that was established, improved, or expanded under this program, deidentified and disaggregated by race, ethnicity, age, sex, geographic region, disability status, medical specialty pursued, and other relevant factors, to the extent such information is available; (C) the effects of such program on the health care provider workforce, including any impact on demographic representation disaggregated by race, ethnicity, and sex, and the fields or specialties pursued by students who have graduated from any school of medicine or osteopathic medicine, or a branch campus of school of medicine or osteopathic medicine, that was established, improved, or expanded under this program; (D) the effects of such program on health care access in underserved areas, including medically underserved communities and health professional shortage areas; and (E) recommendations for improving the program described in this section, and any other considerations as the Secretary determines appropriate. (3) Public availability The Secretary shall make reports submitted under paragraph (2) publicly available on the website of the Department of Health and Human Services. (g) Definitions In this section: (1) Branch campus (A) In general The term branch campus , with respect to a school of medicine or osteopathic medicine, means an additional location of such school that is geographically apart and independent of the main campus, at which the school offers at least 50 percent of the program leading to a degree of doctor of medicine or doctor of osteopathy that is offered at the main campus. (B) Independence from main campus For purposes of subparagraph (A), the location of a school described in such subparagraph shall be considered to be independent of the main campus described in such subparagraph if the location\u2014 (i) is permanent in nature; (ii) offers courses in educational programs leading to a degree, certificate, or other recognized educational credential; (iii) has its own faculty and administrative or supervisory organization; and (iv) has its own budgetary and hiring authority. (2) First generation college student The term first generation college student has the meaning given such term in section 402A(h)(3) of the Higher Education Act of 1965. (3) Health professional shortage area The term health professional shortage area has the meaning given such term in section 332(a). (4) Institution of higher education The term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965. (5) Medically underserved community The term medically underserved community has the meaning given such term in section 799B(6). (h) Authorization of appropriations There is authorized to be appropriated such sums as may be necessary to carry out this section. .",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2106",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expanding Medical Education Act",
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
        "name": "Health",
        "updateDate": "2025-04-04T12:00:31Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s975is.xml"
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
      "title": "Expanding Medical Education Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expanding Medical Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a grant program to support schools of medicine and schools of osteopathic medicine in underserved areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:33Z"
    }
  ]
}
```

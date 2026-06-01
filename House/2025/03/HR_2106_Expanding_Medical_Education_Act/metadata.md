# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2106
- Title: Expanding Medical Education Act
- Congress: 119
- Bill type: HR
- Bill number: 2106
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-01-07T09:05:43Z
- Update date including text: 2026-01-07T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2106",
    "number": "2106",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expanding Medical Education Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:43Z",
    "updateDateIncludingText": "2026-01-07T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:00:20Z",
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
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "TN"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "AL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2106ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2106\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Costa (for himself and Mr. Gray ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish a grant program to support schools of medicine and schools of osteopathic medicine in underserved areas.\n#### 1. Short title\nThis Act may be cited as the Expanding Medical Education Act .\n#### 2. Grants for schools of medicine and schools of osteopathic medicine in underserved areas\nSubpart II of part C of title VII of the Public Health Service Act ( 42 U.S.C. 293m et seq. ) is amended by adding at the end the following:\n749C. Grants for schools of medicine and schools of osteopathic medicine in underserved areas (a) In general The Secretary may award grants to institutions of higher education (including consortiums of such institutions) for the establishment, improvement, or expansion of a school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine. (b) Priority In selecting grant recipients under this section, the Secretary shall give priority to any institution of higher education (or consortium of such institutions) that\u2014 (1) proposes to use the grant for the establishment of a school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine, in an area\u2014 (A) in which\u2014 (i) no other such school is based; or (ii) in the case in which the school of medicine or osteopathic medicine proposed to be established would be a minority-serving institution, no other minority-serving institution that includes a school of medicine or osteopathic medicine is based; and (B) that is a medically underserved community or a health professional shortage area; or (2) is a minority-serving institution described in section 371(a) of the Higher Education Act of 1965 or an institution or program described in section 326(e) of such Act. (c) Considerations In awarding grants under this section, the Secretary, to the extent practicable, may ensure equitable distribution of awards among the geographical regions of the United States. (d) Use of funds An institution of higher education (or a consortium of such institutions)\u2014 (1) shall use grant amounts received under this section to\u2014 (A) recruit, enroll, and retain medical students who are pursuing a degree of doctor of medicine or doctor of osteopathy, including individuals who are from disadvantaged backgrounds (including racial and ethnic groups underrepresented among medical students and health professions), individuals from rural and underserved areas, low-income individuals, and first generation college students, at a school of medicine or osteopathic medicine or branch campus of a school of medicine or osteopathic medicine; and (B) develop, implement, and expand curriculum that emphasizes care for rural and underserved populations, including accessible and culturally and linguistically appropriate care and services, at such school or branch campus; and (2) may use grant amounts received under this section to\u2014 (A) plan and construct\u2014 (i) a school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine, in an area in which no other such school is based; or (ii) a school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine, that will be a minority-serving institution, in an area in which no other such school that is a minority-serving institution is based; (B) plan, develop, and meet criteria for accreditation for a school of medicine or osteopathic medicine or branch campus of a school of medicine or osteopathic medicine; (C) hire faculty, including faculty from racial and ethnic groups who are underrepresented among the medical and other health professions, and other staff to serve at such a school or branch campus; (D) support educational programs at such a school or branch campus; (E) modernize and expand infrastructure at such a school or branch campus; and (F) support other activities that the Secretary determines further the establishment, improvement, or expansion of a school of medicine or osteopathic medicine or branch campus of a school of medicine or osteopathic medicine. (e) Application To be eligible to receive a grant under subsection (a), an institution of higher education (or a consortium of such institutions), shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including a description of the institution\u2019s or consortium's planned activities described in subsection (d). (f) Reporting (1) Reports from entities Each institution of higher education, or consortium of such institutions, awarded a grant under this section shall submit an annual report to the Secretary on the activities conducted under such grant, and other information as the Secretary may require. (2) Report to Congress Not later than 5 years after the date of enactment of this section and every 5 years thereafter, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that provides a summary of the activities and outcomes associated with grants made under this section. Such reports shall include\u2014 (A) a list of awardees, including their primary geographic location, and location of any school of medicine or osteopathic medicine, or a branch campus of school of medicine or osteopathic medicine that was established, improved, or expanded under the program under this section; (B) the total number of students (including the number of students from racial and ethnic groups underrepresented among medical students and health professions, low-income students, and first generation college students) who\u2014 (i) are enrolled at, or who have graduated from, any school of medicine or osteopathic medicine, or a branch campus of school of medicine or osteopathic medicine, that was established, improved, or expanded under the program under this section, deidentified and disaggregated by race, ethnicity, age, sex, geographic region, disability status, and other relevant factors, to the extent such information is available; and (ii) who subsequently participate in an accredited internship or medical residency program upon graduation from any school of medicine or osteopathic medicine, or a branch campus of a school of medicine or osteopathic medicine, that was established, improved, or expanded under the program under this section, deidentified and disaggregated by race, ethnicity, age, sex, geographic region, disability status, medical specialty pursued, and other relevant factors, to the extent such information is available; (C) the effects of such program on the health care provider workforce, including any impact on demographic representation disaggregated by race, ethnicity, and sex, and the fields or specialties pursued by students who have graduated from any school of medicine or osteopathic medicine, or a branch campus of school of medicine or osteopathic medicine, that was established, improved, or expanded under the program under this section; (D) the effects of such program on health care access in underserved areas, including medically underserved communities and health professional shortage areas; and (E) recommendations for improving the program described in this section, and any other considerations as the Secretary determines appropriate. (3) Public availability The Secretary shall make reports submitted under paragraph (2) publicly available on the website of the Department of Health and Human Services. (g) Definitions In this section: (1) Branch campus (A) In general The term branch campus , with respect to a school of medicine or osteopathic medicine, means an additional location of such school that is geographically apart and independent of the main campus, at which the school offers at least 50 percent of the program leading to a degree of doctor of medicine or doctor of osteopathy that is offered at the main campus. (B) Independence from main campus For purposes of subparagraph (A), the location of a school described in such subparagraph shall be considered to be independent of the main campus described in such subparagraph if the location\u2014 (i) is permanent in nature; (ii) offers courses in educational programs leading to a degree, certificate, or other recognized educational credential; (iii) has its own faculty and administrative or supervisory organization; and (iv) has its own budgetary and hiring authority. (2) First generation college student The term first generation college student has the meaning given such term in section 402A(h)(3) of the Higher Education Act of 1965. (3) Health professional shortage area The term health professional shortage area has the meaning given such term in section 332(a). (4) Institution of higher education The term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965. (5) Medically underserved community The term medically underserved community has the meaning given such term in section 799B(6). (h) Authorization of appropriations There is authorized to be appropriated such sums as may be necessary to carry out this section. .",
      "versionDate": "2025-03-14",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-12",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "975",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expanding Medical Education Act",
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
        "name": "Health",
        "updateDate": "2025-04-04T16:19:25Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2106ih.xml"
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
      "title": "Expanding Medical Education Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Medical Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program to support schools of medicine and schools of osteopathic medicine in underserved areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:27Z"
    }
  ]
}
```

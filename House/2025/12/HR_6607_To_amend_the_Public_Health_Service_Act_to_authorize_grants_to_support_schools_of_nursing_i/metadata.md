# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6607?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6607
- Title: FAAN Act
- Congress: 119
- Bill type: HR
- Bill number: 6607
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-04-16T08:06:36Z
- Update date including text: 2026-04-16T08:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6607",
    "number": "6607",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "FAAN Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:36Z",
    "updateDateIncludingText": "2026-04-16T08:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:05:35Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6607ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6607\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Ms. Underwood introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize grants to support schools of nursing in increasing the number of nursing students and faculty and in program enhancement and infrastructure modernization, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Future Advancement of Academic Nursing Act or the FAAN Act .\n#### 2. Support for nursing education and the future nursing workforce\nPart D of title VIII of the Public Health Service Act ( 42 U.S.C. 296p et seq. ) is amended by adding at the end the following:\n832. Nursing education enhancement and modernization grants in underserved areas (a) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration, may award grants to schools of nursing for\u2014 (1) increasing the number of faculty and students at such schools in order to address nursing workforce shortages; (2) expanding the capacity of such schools to enhance the preparedness of the United States for, and the ability of the United States to address and quickly respond to, public health emergencies declared under section 319 and pandemics that are not otherwise declared as such emergencies; or (3) the enhancement and modernization of nursing education programs. (b) Priority In selecting grant recipients under this section, the Secretary shall give priority to schools of nursing that\u2014 (1) are located in, or prepare students to practice in, a medically underserved area (as defined in section 330I(a)); (2) are located in, or prepare students to practice in, a health professional shortage area as defined under section 332(a); (3) are institutions of higher education listed under section 371(a) of the Higher Education Act of 1965; or (4) are located in, or prepare students to practice in, a rural area or a noncontiguous State or territory of the United States. (c) Consideration In awarding grants under this section, the Secretary, to the extent practicable, may ensure equitable distribution of awards among the geographic regions of the United States. (d) Use of funds A school of nursing that receives a grant under this section shall use the funds awarded through such grant for activities that include\u2014 (1) enhancing enrollment and retention of students at such school, with a priority for students from disadvantaged backgrounds (including racial or ethnic groups underrepresented in the nursing workforce), individuals from rural and underserved areas, low-income individuals, and first generation college students (as defined in section 402A(h)(3) of the Higher Education Act of 1965), including through mentorship programs, providing tools and programming for underrepresented students, and addressing other student needs; (2) retaining current faculty, and hiring new faculty, with an emphasis on faculty from racial or ethnic groups who are underrepresented in the nursing workforce; (3) partnering with a health care facility, nurse-managed health clinic, community health center, or other facility that provides health care in order to provide educational opportunities for the purpose of establishing or expanding clinical education, including through preceptors; (4) modernizing infrastructure at such school, including audiovisual or other equipment, simulation and augmented reality resources, telehealth technologies, and virtual and physical laboratories; (5) creating, supporting, or modernizing educational programs and curriculum at such school; (6) enhancing and expanding nursing programs that prepare nurse researchers and scientists; (7) establishing nurse-led intradisciplinary and interprofessional educational partnerships; or (8) other activities that the Secretary determines further the development, improvement, and expansion of schools of nursing. (e) Reports from entities Each school of nursing awarded a grant under this section shall submit an annual report to the Secretary on the activities conducted under such grant, and other information as the Secretary may require. (f) Report to Congress Not later than 5 years after the date of the enactment of this section, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives, and make publicly available, a report that provides a summary of the activities and outcomes associated with grants made under this section. Such report shall include\u2014 (1) a list of schools of nursing receiving grants under this section, including the primary geographic location of any school of nursing that was improved or expanded through such a grant; (2) the total number of students who are enrolled at or who have graduated from any school of nursing that was improved or expanded through a grant under this section, which such statistic shall\u2014 (A) to the extent such information is available, be deidentified and disaggregated by race, ethnicity, age, sex, geographic region, disability status, and other relevant factors; and (B) include an indication of the number of such students who are from racial or ethnic groups underrepresented in the nursing workforce, such students who are from rural or underserved areas, such students who are low-income students, and such students who are first generation college students (as defined in section 402A(h)(3) of the Higher Education Act of 1965); (3) to the extent such information is available\u2014 (A) the effects of the grants awarded under this section on\u2014 (i) retaining and hiring of faculty, including any increase in diverse faculty; (ii) the number of clinical education partnerships; and (iii) the modernization of nursing education infrastructure; and (B) other ways this section helps to address nursing workforce shortages and quickly respond to public health emergencies declared under section 319 and pandemics that are not otherwise declared as such emergencies; (4) recommendations for improving the grants awarded under this section; and (5) any other considerations as the Secretary determines appropriate. (g) Authorization of appropriations To carry out this section, there is authorized to be appropriated $1,000,000,000 to remain available until expended. .\n#### 3. Strengthening nurse education\nThe heading of part D of title VIII of the Public Health Service Act ( 42 U.S.C. 296p et seq. ) is amended by striking Basic .",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3435",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAAN Act",
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
        "updateDate": "2026-01-07T17:53:25Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6607ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize grants to support schools of nursing in increasing the number of nursing students and faculty and in program enhancement and infrastructure modernization, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:24Z"
    },
    {
      "title": "FAAN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAAN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Future Advancement of Academic Nursing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:21Z"
    }
  ]
}
```

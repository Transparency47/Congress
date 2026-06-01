# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3435?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3435
- Title: FAAN Act
- Congress: 119
- Bill type: S
- Bill number: 3435
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-07T17:53:47Z
- Update date including text: 2026-01-07T17:53:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3435",
    "number": "3435",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "FAAN Act",
    "type": "S",
    "updateDate": "2026-01-07T17:53:47Z",
    "updateDateIncludingText": "2026-01-07T17:53:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:45:25Z",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NM"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "HI"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-12-11",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-11",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3435is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3435\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Merkley (for himself, Mr. Schiff , Mr. Blumenthal , Mr. Booker , Ms. Duckworth , Mr. Fetterman , Mr. Heinrich , Ms. Hirono , Mr. King , Ms. Klobuchar , Mr. Padilla , Mr. Sanders , Ms. Smith , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to authorize grants to support schools of nursing in increasing the number of nursing students and faculty and in program enhancement and infrastructure modernization, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Future Advancement of Academic Nursing Act or the FAAN Act .\n#### 2. Support for nursing education and the future nursing workforce\nPart D of title VIII of the Public Health Service Act ( 42 U.S.C. 296p et seq. ) is amended by adding at the end the following:\n832. Nursing education enhancement and modernization grants in underserved areas (a) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration, may award grants to schools of nursing for\u2014 (1) increasing the number of faculty and students at such schools in order to address nursing workforce shortages; (2) expanding the capacity of such schools to enhance the preparedness of the United States for, and the ability of the United States to address and quickly respond to, public health emergencies declared under section 319 and pandemics that are not otherwise declared as such emergencies; or (3) the enhancement and modernization of nursing education programs. (b) Priority In selecting grant recipients under this section, the Secretary shall give priority to schools of nursing that\u2014 (1) are located in, or prepare students to practice in, a medically underserved area (as defined in section 330I(a)); (2) are located in, or prepare students to practice in, a health professional shortage area as defined under section 332(a); (3) are institutions of higher education listed under section 371(a) of the Higher Education Act of 1965; or (4) are located in, or prepare students to practice in, a rural area or a noncontiguous State or territory of the United States. (c) Consideration In awarding grants under this section, the Secretary, to the extent practicable, may ensure equitable distribution of awards among the geographic regions of the United States. (d) Use of funds A school of nursing that receives a grant under this section shall use the funds awarded through such grant for activities that include\u2014 (1) enhancing enrollment and retention of students at such school, with a priority for students from disadvantaged backgrounds (including racial or ethnic groups underrepresented in the nursing workforce), individuals from rural and underserved areas, low-income individuals, and first generation college students (as defined in section 402A(h)(3) of the Higher Education Act of 1965), including through mentorship programs, providing tools and programming for underrepresented students, and addressing other student needs; (2) retaining current faculty, and hiring new faculty, with an emphasis on faculty from racial or ethnic groups who are underrepresented in the nursing workforce; (3) partnering with a health care facility, nurse-managed health clinic, community health center, or other facility that provides health care in order to provide educational opportunities for the purpose of establishing or expanding clinical education, including through preceptors; (4) modernizing infrastructure at such school, including audiovisual or other equipment, simulation and augmented reality resources, telehealth technologies, and virtual and physical laboratories; (5) creating, supporting, or modernizing educational programs and curriculum at such school; (6) enhancing and expanding nursing programs that prepare nurse researchers and scientists; (7) establishing nurse-led intradisciplinary and interprofessional educational partnerships; or (8) other activities that the Secretary determines further the development, improvement, and expansion of schools of nursing. (e) Reports from entities Each school of nursing awarded a grant under this section shall submit an annual report to the Secretary on the activities conducted under such grant, and other information as the Secretary may require. (f) Report to Congress Not later than 5 years after the date of the enactment of this section, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives, and make publicly available, a report that provides a summary of the activities and outcomes associated with grants made under this section. Such report shall include\u2014 (1) a list of schools of nursing receiving grants under this section, including the primary geographic location of any school of nursing that was improved or expanded through such a grant; (2) the total number of students who are enrolled at or who have graduated from any school of nursing that was improved or expanded through a grant under this section, which such statistic shall\u2014 (A) to the extent such information is available, be deidentified and disaggregated by race, ethnicity, age, sex, geographic region, disability status, and other relevant factors; and (B) include an indication of the number of such students who are from racial or ethnic groups underrepresented in the nursing workforce, such students who are from rural or underserved areas, such students who are low-income students, and such students who are first generation college students (as defined in section 402A(h)(3) of the Higher Education Act of 1965); (3) to the extent such information is available\u2014 (A) the effects of the grants awarded under this section on\u2014 (i) retaining and hiring of faculty, including any increase in diverse faculty; (ii) the number of clinical education partnerships; and (iii) the modernization of nursing education infrastructure; and (B) other ways this section helps to address nursing workforce shortages and quickly respond to public health emergencies declared under section 319 and pandemics that are not otherwise declared as such emergencies; (4) recommendations for improving the grants awarded under this section; and (5) any other considerations as the Secretary determines appropriate. (g) Authorization of appropriations To carry out this section, there is authorized to be appropriated $1,000,000,000 to remain available until expended. .\n#### 3. Strengthening nurse education\nThe heading of part D of title VIII of the Public Health Service Act ( 42 U.S.C. 296p et seq. ) is amended by striking Basic .",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-11",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6607",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAAN Act",
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
        "updateDate": "2026-01-07T17:53:47Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3435is.xml"
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
      "title": "FAAN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FAAN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Future Advancement of Academic Nursing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to authorize grants to support schools of nursing in increasing the number of nursing students and faculty and in program enhancement and infrastructure modernization, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:29Z"
    }
  ]
}
```

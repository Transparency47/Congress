# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8355?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8355
- Title: Accountable Produce is Medicine Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8355
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-05-20T08:08:16Z
- Update date including text: 2026-05-20T08:08:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8355",
    "number": "8355",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Accountable Produce is Medicine Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:16Z",
    "updateDateIncludingText": "2026-05-20T08:08:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-16T14:06:35Z",
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
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "KS"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "KS"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8355ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8355\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Smucker (for himself and Ms. Davids of Kansas ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XI of the Social Security Act to require the Center for Medicare and Medicaid Innovation to test a model to reduce chronic diseases by using accountable produce is medicine.\n#### 1. Short title\nThis Act may be cited as the Accountable Produce is Medicine Act of 2026 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\ndiet-related chronic diseases are a leading driver of health care costs in the United States;\n**(2)**\nevidence-based food is medicine interventions, including medically tailored meals, medically tailored groceries, produce prescriptions, and nutrition counseling, have the potential to improve health outcomes and reduce health care expenditures;\n**(3)**\nthe Center for Medicare and Medicaid Innovation should, to the extent practicable, incorporate such interventions, as appropriate, into models tested under section 1115A of the Social Security Act ( 42 U.S.C. 1315a ); and\n**(4)**\nincorporating food is medicine interventions into Innovation Center models may improve quality of care, reduce costs, and support the prevention and management of chronic disease.\n#### 3. Requiring the Center for Medicare and Medicaid Innovation to test a model to improve outcomes for patients with chronic diseases by using accountable produce is medicine\nSection 1115A of the Social Security Act ( 42 U.S.C. 1315a ) is amended\u2014\n**(1)**\nin subsection (b)(2)(A), by inserting , and, beginning not later than the date that is 180 days after the enactment of the Accountable Produce is Medicine Act of 2026 , shall include the Accountable Produce is Medicine Bundled Payment Model described in subsection (h) before the period at the end; and\n**(2)**\nby adding at the end the following new subsection:\n(h) Accountable Produce is Medicine Bundled Payment Model (1) In general For purposes of subsection (b)(2)(A), the Accountable Produce is Medicine Bundled Payment Model described in this subsection is a model under which bundled payment is made under title XVIII, title XIX, or title XXI, as appropriate, for selected programs to furnish Accountable Produce is Medicine services to eligible individuals. (2) Selection of programs to participate (A) Selected programs The Secretary shall select to participate in the model described under paragraph (1) at least 5 eligible programs, each to participate for a period of not less than 2 years, that the Secretary determines have the capacity to satisfy the requirements described in paragraph (3) . In this subsection, each such eligible program so selected shall be referred to as a selected program . (B) Priority In selecting eligible programs under subparagraph (A) , the Secretary shall give priority to any such program that furnishes (including through an arrangement with a provider of services or supplier or other entity) fresh, frozen, or minimally processed fruits and vegetables without added sugars, sodium, or saturated fats (except those occurring naturally), and other plant-based, nutrient-dense foods, including nuts, seeds, intact whole grains, beans, and lentils. (3) Minimum program requirements Under the model under paragraph (1) , a selected program shall comply with each of the following requirements: (A) Screening The selected program shall screen individuals who are referred to the program by a physician, hospital, or other health care provider, to determine whether such individuals are eligible individuals. (B) Accountable Produce is Medicine services In the case of an individual who is determined by the selected program under subparagraph (A) to be an eligible individual, the selected program shall, for the 1-year period following such determination (subject to subparagraph (D) ), make available (including through an arrangement with a provider of services or supplier or other entity) to such individual the following services (in this subsection referred to as Accountable Produce is Medicine services or APIM services ): (i) A personalized health risk assessment and personalized prevention plan services. (ii) Care coordination services. (iii) Telehealth services related to chronic disease monitoring, education, and follow-up. (iv) Remote patient monitoring items and services that are clinically appropriate for chronic disease monitoring and facilitate a timely response from a provider in the case that significant changes in such data are detected. (v) Lifestyle modification programs, including nutrition counseling provided by a registered dietician or other qualified provider, exercise programs, and smoking cessation counseling. (vi) Healthy, nutrient-dense foods meeting such standards as the Secretary shall determine, with preference given to produce grown within 250 miles of the selected program or through the use of regenerative agriculture. (C) Collection of health data; reenrollment assessment In the case of an individual who is determined by the selected program under subparagraph (A) to be an eligible individual, the selected program shall\u2014 (i) track the APIM services that the individual has received from the program under the model; (ii) regularly evaluate the individual\u2019s engagement with the program and adherence to program requirements; (iii) on a quarterly basis collect from such individual updated weight, blood pressure, and blood glucose measurements, and any other measurements determined appropriate by the Secretary; and (iv) at the end of the 1-year period described in subparagraph (B) \u2014 (I) evaluate the measurements collected under clause (iii) ; (II) submit to the Secretary such data as the Secretary determines necessary for purposes of evaluating the health care cost savings achieved for such individual during such period; and (III) provide for an additional determination under subparagraph (A) as to whether such individual remains an eligible individual. (D) Disenrollment In the case of an individual who is determined by the selected program under subparagraph (A) to be an eligible individual, if the selected program determines (in accordance with standards established by the Secretary) before the end of the 1-year period described in subparagraph (B) that such individual is not adequately engaging with the program or is not adhering to program requirements, the selected program shall terminate the individual\u2019s participation in the program and may not furnish any additional APIM services to such individual under the model. (4) Payment (A) In general The Secretary shall determine the form, manner, and amount of bundled payment to be provided to selected programs under the model under paragraph (1) and, beginning in the third year in which such model is carried out, may require that selected programs assume financial risk for performance under the model. (B) Cost sharing APIM services furnished by a selected program to an eligible individual shall be provided without application of deductibles, copayments, coinsurance, or other cost-sharing under the applicable title. (5) Duration The model described in paragraph (1) shall be carried out for a period of not less than 5 years. (6) Definitions In this subsection: (A) Eligible individual The term eligible individual means an individual\u2014 (i) who is\u2014 (I) entitled to benefits under part A of title XVIII or enrolled under part B of such title; (II) enrolled under a State plan (or waiver of such plan) under title XIX; or (III) enrolled under a State child health plan (or waiver of such plan) under title XXI; (ii) who resides in a medically underserved area (as designated pursuant to section 330(b)(3)(A) of the Public Health Service Act), a rural area (as defined in section 1886(d)(2)(D)), a health professional shortage area described in section 332(a)(1)(A) of the Public Health Service Act, or another area determined appropriate by the Secretary; (iii) who has diabetes, obesity, cardiovascular disease, hypertension, malnutrition, or any other disease or chronic condition that the Secretary determines appropriate; (iv) in the clinical judgment of a physician or other health care professional, who would benefit from participation in the model; (v) who the eligible program determines to be prepared to participate in the model; and (vi) who is not already receiving items or services that the Secretary determines are substantially similar (and duplicative in purpose and clinical function) to the APIM services described in clause (v) of paragraph (3)(B) . (B) Eligible program The term eligible program means a provider of services or supplier enrolled in the program under title XVIII, title XIX, or title XXI. (C) Regenerative agriculture The term regenerative agriculture means a conservation management approach that emphasizes natural resources through improved soil health, water management, and natural vitality. .",
      "versionDate": "2026-04-16",
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
        "name": "Health",
        "updateDate": "2026-04-28T15:48:07Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8355ih.xml"
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
      "title": "Accountable Produce is Medicine Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accountable Produce is Medicine Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XI of the Social Security Act to require the Center for Medicare and Medicaid Innovation to test a model to reduce chronic diseases by using accountable produce is medicine.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:30Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3643
- Title: VA Data Transparency and Trust Act
- Congress: 119
- Bill type: HR
- Bill number: 3643
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-04-10T16:52:39Z
- Update date including text: 2026-04-10T16:52:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Health.
- 2025-06-12 - Committee: Subcommittee Hearings Held
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Health.
- 2025-06-12 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3643",
    "number": "3643",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001239",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. McGuire, John J. [R-VA-5]",
        "lastName": "McGuire",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "VA Data Transparency and Trust Act",
    "type": "HR",
    "updateDate": "2026-04-10T16:52:39Z",
    "updateDateIncludingText": "2026-04-10T16:52:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-12T16:43:18Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-06T16:43:01Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "IL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "NY"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "VA"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TX"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "CO"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "OK"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3643ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3643\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. McGuire (for himself and Mr. Bost ) introduced the following bill; which was referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to improve the annual reports submitted to Congress with respect to the Veterans Benefits Administration and the Veterans Health Administration, and for other purposes.\n#### 1. Short Title\nThis Act may be cited as the VA Data Transparency and Trust Act .\n#### 2. Improvements to annual reports on the Veterans Benefits Administration and the Veterans Health Administration\n##### (a) VHA report\nSection 7330B of title 38, United States Code, is amended to read as follows:\n7330B. Annual report on Veterans Health Administration and furnishing of hospital care, medical services, and nursing home care (a) Report required During the period beginning on the date of the enactment of the VA Data Transparency and Trust Act and ending on the date that is five years after such date, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report on, for the calendar year preceding the calendar year during which the report is submitted\u2014 (1) the furnishing of hospital care, medical services, and nursing home care under the laws administered by the Secretary; and (2) the administration of the furnishing of such care and services by the Veterans Health Administration. (b) Elements Each report required by subsection (a) shall include each of the following for the year covered by the report: (1) The total number of veterans who received hospital care, medical services, and nursing home care under the laws administered by the Secretary furnished by the Veterans Health Administration. (2) Information with respect to the health status of veterans described in paragraph (1), that includes the rate of incidence among such veterans of major chronic conditions, disaggregated by condition, including\u2014 (A) traumatic brain injury; (B) diabetes; (C) cardiovascular disease; and (D) cancer. (3) Demographic information with respect to such veterans, disaggregated by\u2014 (A) age; (B) period of\u2014 (i) active military, naval, air, or space service; or (ii) service in a Reserve component; and (C) sex. (4) Information with respect to furnishing of health care during the period covered by the report to\u2014 (A) veterans who served on active duty during the Post-9/11 Global Operations period (as defined in section 3105 of this title), including\u2014 (i) a summary of conditions the Secretary determines are commonly present in such veterans; (ii) a summary of common conditions in such veterans that the Secretary determines have arisen since the date of the submission of the preceding report; (iii) an estimate of the number of such veterans that belong to a different priority group specified in subsection (a) of section 1705 of this title than on the date of the submission of the preceding report; and (iv) an estimate of the number of such veterans who are enrolled in a health insurance plan that is not a health insurance plan under the laws administered by the Secretary; (B) veterans with mental health conditions (including traumatic brain injury and suicidal ideation); (C) veterans with polytrauma; (D) veterans with spinal cord injury or dysfunction; (E) veterans with service-connected disabilities, including the average cost to the Department of furnishing such care to such veterans; and (F) homeless veterans, including\u2014 (i) the average age of such veterans; (ii) estimates of the geographic locations of such veterans; (iii) estimates of the average duration of homelessness for such veterans; and (iv) the periods during which such veterans performed active military, naval, air, or space service. (5) Information with respect to veterans who received long term care under the laws administered by the Secretary during the period covered by the report, including\u2014 (A) the demographic information of such veterans, including common chronic illnesses present in such veterans; (B) the average amount of copayments for such long term care made by such veterans; (C) a description of the types of such long term care; and (D) funding levels for State homes as of the date of the submission of the report. (6) The number of veterans who enrolled in the annual system for patient enrollment under section 1705 of this title during the period covered by the report, disaggregated by\u2014 (A) priority group specified in subsection (a) of such section; (B) age; (C) sex; (D) annual income; and (E) enrollment in a health insurance plan that is not a health insurance plan under the laws administered by the Secretary. (7) With respect to veterans described in paragraph (6), the average period of time between the date on which such a veteran was separated from active military, naval, air, or space service and the earlier of\u2014 (A) the date on which the veteran enrolled in such annual system for patient enrollment; and (B) the date on which the veteran first received hospital care, medical services, or nursing home care under the laws administered by the Secretary furnished by the Veterans Health Administration. (8) The total number of visits to facilities of the Department for hospital care, medical services, and nursing home care under laws administered by the Secretary. (9) A summary of each type of hospital care, medical service, or nursing home care under laws administered by the Secretary furnished by the Veterans Health Administration to veterans, including\u2014 (A) inpatient care; (B) outpatient care; (C) prescription drugs; (D) mental health care; and (E) primary care. (10) A statement of the percentage of hospital care, medical service, or nursing home care under laws administered by the Secretary furnished by the Veterans Health Administration to veterans during the period covered by the report intended to treat\u2014 (A) service-connected disabilities; and (B) non-service-connected disabilities. (11) With respect to prescription drugs and medicines furnished to veterans by the Veterans Health Administration during the period covered by the report, a statement of\u2014 (A) the total number of such prescriptions for such drugs and medicine dispensed to veterans\u2014 (i) during the course of inpatient care at a facility of the Department; (ii) at a community-based outpatient clinic of the Department; (iii) at a non-Department facility; and (iv) through a mail-order prescription; and (B) the average term of a prescription for each drug or medicine furnished to a veteran by the Veterans Health Administration during such period. (12) With respect to inpatient care provided to veterans at facilities of the Department\u2014 (A) the average length of stay at such a facility for a veteran in receipt of such inpatient care; and (B) the average cost to a veteran of such inpatient care. (13) A summary of diagnostic services provided to veterans during by the report that includes\u2014 (A) a statement of the percentage of such diagnostic services provided for\u2014 (i) a service-connected disability; and (ii) a non-service connected disability; and (B) a description of conditions diagnosed pursuant to such diagnostic services, disaggregated by body system associated with such condition. (14) An assessment of the extent to which veterans who received hospital care, medical services, and nursing home care furnished by the Veterans Health Administration during the period covered by the report rely on the Veterans Health Administration for health care, disaggregated by veterans\u2014 (A) who are\u2014 (i) younger than 65 years of age; (ii) 65 years of age or older; (iii) fully reliant on the Veterans Health Administration; (iv) partially reliant on the Veterans Health Administration; and (v) not reliant on the Veterans Health Administration; (B) who received\u2014 (i) inpatient care; and (ii) outpatient care. (15) An assessment of the quality of health care furnished to veterans by the Veterans Health Administration that includes a measurement of\u2014 (A) the incidence of hospital acquired infections among veterans; (B) the extent to which veterans are satisfied with such health care, disaggregated by such health care provided at\u2014 (i) a facility of the Department; and (ii) a non-Department facility. (16) A summary of the hospital care, medical services, and nursing home care furnished by the Veterans Health Administration\u2014 (A) required under VA MISSION Act of 2018 ( Public Law 115\u2013182 ; 38 U.S.C. 301 note); (B) required under the Honoring our PACT Act of 2022 ( Public Law 117\u2013168 ); (C) under section 1781 of this title, that includes an estimate of the average cost to the Department of furnishing such care, disaggregated by the age of the individual to which such care was furnished; and (D) under section 1703 of this title. (17) A summary of collections of copayments for health care under the laws administered by the Secretary that includes\u2014 (A) a statement of the percentage of such copayments made by\u2014 (i) veterans; and (ii) third parties; and (B) a comparison of such collections to health care billings owed to the Department. (18) Data with respect to the Medical Care Collections Fund established under section 1729A of this title that includes, with respect to the period covered by the report\u2014 (A) an identification of the total number of veterans from whom amounts were collected; (B) the average amount so collected\u2014 (i) per veteran; and (ii) per priority group specified in subsection (a) of section 1705 of this title; and (C) the total amount so collected. (19) Information with respect to physicians employed by the Veterans Health Administration, that includes\u2014 (A) the number of such physicians who are full-time employees, disaggregated by\u2014 (i) specialty; and (ii) the type of medical facility where the physician is employed; (B) the average annual salary for such physicians, including bonuses and other pay awards; and (C) for such physicians who are primary care physicians\u2014 (i) the average number of patients, adjusted for patient health status, treated per\u2014 (I) week; and (II) calendar year; and (ii) the average amount of time such physicians spend with patients during appointments for primary care. (20) Information with respect to medical professionals employed by the Veterans Health Administration that includes a statement of\u2014 (A) the average number of patients such a medical professional treats each week; and (B) the average amount of time such physicians spend with patients during appointments for primary care. (21) An assessment of the management of facilities of Veterans Health Administration that includes\u2014 (A) for each medical facility under the jurisdiction of the Veterans Health Administration a statement of\u2014 (i) the date of\u2014 (I) the original construction; and (II) the most recent renovation project carried out, if applicable; (ii) the total square feet; (iii) the cost to the Department of regular maintenance and repairs; (B) for each such medical facility that provides inpatient care, the rate of occupancy; and (C) for each such medical facility that provides outpatient care, the number of patient visits, disaggregated by type of health care provided at the visit. (22) A summary of major capital spending pursuant to the administration by the Veterans Health Administration of furnishing medical care and services under the laws administered by the Secretary that includes a description of\u2014 (A) planned construction of new facilities; (B) planned renovation of facilities; and (C) any purchase of medical equipment that totals more than $20,000. (23) For each priority group specified in subsection (a) of section 1705 of this title\u2014 (A) demographic information of veterans that comprise each such priority group; (B) an assessment of the extent to which veterans that comprise each such priority group use the benefits under the laws administered by the Secretary for which such veterans are eligible; and (C) an estimate of the average cost to the Department of furnishing health care under the laws administered by the Secretary to veterans that comprise each such priority group. (24) The percentage of hospital care, medical services, and nursing home care provided to veterans in facilities of the Department and in non-Department facilities and any changes in such percentages compared to the year preceding the year covered by the report. (c) Data sharing system (1) The Secretary shall develop and carry out a data sharing system to grant individuals described in paragraph (2) access to aggregated, anonymized data with respect to veterans and individuals receiving health care furnished under laws administered by the Secretary. (2) An eligible individual described in this paragraph is a researcher who meets the criteria for data security and data protection established by the Secretary in regulations for the purposes of administering the data sharing system under paragraph (1). (3) In developing the data sharing system under paragraph (1), the Secretary shall consider the Centers for Medicare & Medicaid Services Qualified Entity Program (commonly referred to as the Medicare Data Sharing for Performance Measurement Program ) established pursuant to section 1874(e) of the Social Security Act ( 42 U.S.C. 1395kk(e) , 1395kk\u20132). (4) The Secretary shall ensure that data available through such data sharing system includes\u2014 (A) each type data available under the Medicare Data Sharing for Performance Measurement Program, where applicable; (B) data on veterans enrolled in the annual system for patient enrollment established under section 1705 of this title, including\u2014 (i) demographic data; (ii) the number of veterans that comprise each priority group specified in subsection (a) of such section; and (iii) the number of veterans with service-connected disabilities, disaggregated by level of disability rating determined by the Secretary; (C) data on visits for health care under laws administered by the Secretary furnished at facilities of the Department, including\u2014 (i) types of health care providers furnishing such health care during such visits; (ii) diagnostic codes associated with illnesses in veterans diagnosed during the course of such visits; (iii) with respect to such visits for outpatient care, an identification of the date of such visit; and (iv) with respect to such visits for inpatient care, an identification of the applicable admission date and discharge date; and (D) data on insurance claims submitted to the Secretary for health care furnished at non-Department facilities, including\u2014 (i) provider numbers of applicable insurance companies; (ii) payments made by the Secretary to veterans pursuant to such claims; and (iii) payments made by veterans with respect to such insurance claims. (d) Definitions In this section, the terms hospital care , medical services , nursing home care , facilities of the Department , and non-Department facilities have the meanings given those terms in section 1701 of this title. .\n##### (b) Additional data for inclusion in annual VBA report\nSubchapter II of chapter 77 of title 38, United States Code, is amended by adding at the end the following new section (and conforming the table of sections at the beginning of such chapter accordingly):\n7735. Additional data for inclusion in annual report to Congress; data sharing system (a) In general (1) During the period beginning on the date of the enactment of the VA Data Transparency and Trust Act and ending on the date that is five years after such date, the Secretary shall include in the Annual Benefits Report of the Veterans Benefits Administration the following: (A) The number of veterans in receipt of benefits under the laws administered by the Secretary, disaggregated by\u2014 (i) age; (ii) income level; (iii) period and length of\u2014 (I) active military, naval, air, or space service; or (II) service in a Reserve component. (B) A summary of the types of benefits under the laws administered by the Secretary furnished to veterans. (C) Demographic data with respect to veterans with service-connected disabilities, disaggregated by each schedule of disability rating specified in section 1155 of this title, including\u2014 (i) age; (ii) sex; (iii) race; (iv) highest level of educational attainment; (v) period and length of\u2014 (I) active military, naval, air, or space service; or (II) service in a Reserve component. (D) A statement of the number of veterans with service-connected disabilities to whom the Secretary assigned a disability rating different from the disability rating initially assigned to the veteran. (E) The average amount of compensation under chapter 11 of this title paid to veterans\u2014 (i) with dependents; (ii) in receipt of special monthly compensation under subsection (r) of section 1114 of this title; and (iii) with a disability rated as total by reason of unemployability under section 1164 of this title. (F) Data with respect to veterans with disability ratings reevaluated by the Secretary, including\u2014 (i) the number of such veterans; (ii) the conditions associated with such disability ratings; (iii) the number of such veterans assigned, pursuant to such reevaluation\u2014 (I) an increased disability rating; or (II) a decreased disability rating. (G) For each of fiscal years 1997 through 2024, a statement of the number of reevaluations of disability ratings initiated by the Secretary. (H) For each condition for which a presumption of service-connection is established under chapter 11 of this title\u2014 (i) the number of veterans with such condition in receipt of compensation under such chapter, disaggregated by each schedule of disability rating specified in section 1155; and (ii) the average amount of such compensation paid to such veterans. (I) For each non-service-connected disability that is compensable under the laws administered by the Secretary, a statement of the average amount of compensation under chapater 11 of this title paid to veterans with each such non-service-connected disability. (J) Data with respect to veterans in receipt of a pension under chapter 15 of this title, including\u2014 (i) the number of such veterans, disaggregated by\u2014 (I) age; (II) sex; (III) income level; (IV) period and length of\u2014 (aa) active military, naval, air, or space service; or (bb) service in a Reserve component; (ii) the average period of time between the date on which such a veteran was separated from active military, naval, air, or space service and the date on which the veteran received the first payment of pension under such chapter; and (iii) for each of fiscal years 2000 through 2024, the average amount of pension paid to such veterans. (K) Data with respect to individuals in receipt of dependency and indemnity compensation under chapter 13 of this title, including\u2014 (i) demographic data; and (ii) a summary of the reasons such individuals are eligible for such dependency and indemnity compensation. (L) The number of new claims for disability compensation under the laws administered by the Secretary, and the average period of time between the date on which such claim was submitted and the date on which the Secretary issued a decision with respect to such claim. (M) The number of supplemental claims for disability compensation under such laws, and the average period of time between the date on which such claim was submitted and the date on which the Secretary issued a decision with respect to such claim. (N) Data on the staffing levels of the Veterans Benefits Administration, including the number of full-time employees of the Veterans Benefits Administration responsible for processing such claims for disability compensation. (O) A statement, for each of fiscal years 2000 through 2024, of the average amount of disability compensation under chapter 11 of this title paid to veterans with service-connected disabilities, disaggreated by each schedule of rating specified in section 1155 of this title. (2) (A) The first report submitted pursuant to subsection (a) shall include each element specified in paragraphs (1) through (15) of such subsection for\u2014 (i) the calendar year during which the first report is submitted; and (ii) each calendar year during the five-year period that precedes the date of the submission of the first report. (B) Each report submitted after the date on which the first report is submitted shall include each such element for the calendar year during which the report is submitted. (b) Data sharing system (1) During the period the requirement under subsection (a) is in effect, the Secretary shall develop and carry out a data sharing system to grant eligible individuals described in paragraph (2) access to individual-level, anonymized data with respect to individuals in receipt of benefits furnished by the Under Secretary for Benefits. (2) An eligible individual described in this paragraph is researcher who meets the criteria for data security and data protection established by the Secretary in regulations for the purposes of administering the data sharing system under paragraph (1). (3) Data available through such data sharing system shall include, for each individual in receipt of benefits furnished by the Under Secretary for Benefits\u2014 (A) demographic information, including\u2014 (i) age; (ii) sex; (iii) race; (iv) period and length of\u2014 (I) active military, naval, air, or space service; or (II) service in a Reserve component; (v) branch of service in the Armed Forces; (vi) number of dependents; and (vii) State of residence; (B) information with respect to each service-connected disability for which the individual has filed a claim for disability compensation under laws administered by the Secretary, including\u2014 (i) whether such claim was\u2014 (I) approved by the Secretary; or (II) denied by the Secretary; (ii) the diagnostic code for the service-connected disability; and (iii) the date on which\u2014 (I) the individual filed such claim; and (II) the Secretary issued a decision under section 511 of this title with respect to such claim; and (C) a description of any compensation under the laws administered by the Secretary receives on annual basis, including\u2014 (i) disability compensation; (ii) dependency and indemnity compensation; (iii) educational benefits; (iv) benefits under chapter 37 of this title; (v) special monthly compensation under subsection (r) of section 1114 of this title; and (vi) compensation for a disability rated as total by reason of unemployability under section 1164 of this title. (4) In carrying out such data sharing system, the Secretary shall ensure that\u2014 (A) no personally identifiable information about an individual in receipt of benefits furnished by the Under Secretary for Benefits is accessible through such data sharing system; and (B) each individual about whom data is available under the data sharing system is assigned a unique identifier for use in such data sharing system. .",
      "versionDate": "2025-05-29",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Census and government statistics",
            "updateDate": "2025-06-20T18:32:10Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-20T18:31:54Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T16:52:39Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-06-20T18:32:16Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-06-20T18:31:58Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-20T18:32:06Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-20T18:32:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-10T22:46:59Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3643ih.xml"
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
      "title": "VA Data Transparency and Trust Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T08:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Data Transparency and Trust Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T08:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the annual reports submitted to Congress with respect to the Veterans Benefits Administration and the Veterans Health Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T08:48:21Z"
    }
  ]
}
```

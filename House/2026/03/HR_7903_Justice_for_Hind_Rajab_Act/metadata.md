# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7903?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7903
- Title: Justice for Hind Rajab Act
- Congress: 119
- Bill type: HR
- Bill number: 7903
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-04-29T08:07:14Z
- Update date including text: 2026-04-29T08:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7903",
    "number": "7903",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000305",
        "district": "51",
        "firstName": "Sara",
        "fullName": "Rep. Jacobs, Sara [D-CA-51]",
        "lastName": "Jacobs",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Justice for Hind Rajab Act",
    "type": "HR",
    "updateDate": "2026-04-29T08:07:14Z",
    "updateDateIncludingText": "2026-04-29T08:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:31:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-12T13:31:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "WA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "MI"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7903ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7903\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Ms. Jacobs (for herself, Mr. Castro of Texas , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo call for accountability for the killing of innocent civilians, including 5-year-old Hind Rajab and 2 paramedics, in an attack in Gaza City on January 29, 2024, by Israel Defense Forces, to require the Secretary of State to report to Congress on the attack and to determine if any of the weapons and munitions used in the attack were provided by the United States or if any of the soldiers responsible for such killings were United States citizens or were trained by the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for Hind Rajab Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSince October 7, 2023, the United States has provided more than $21,700,000,000 in military assistance to Israel, which has funded a majority of expenses of the Israel Defense Forces to conduct the war in Gaza.\n**(2)**\nAccording to information from Government of Israel, an estimated 10,000 people from the United States were activated for the war in Gaza.\n**(3)**\nAccording to reports from the Gaza Ministry of Health, more than 20,000 children have been killed in Gaza since October 7, 2023.\n**(4)**\nSince October 7, 2023, at least 1,700 health workers have been killed in Gaza.\n**(5)**\nOn January 29, 2024, 5-year-old Hind Rami Iyad Rajab, along with 6 members of her extended family, were killed in a passenger car by Israel Defense Forces (referred to in this Act as IDF ) tank and machine gun fire while she and her family were fleeing fighting in Gaza City.\n**(6)**\nA forensic investigation conducted by Forensic Architecture discovered a total of 335 bullet holes in the car in which Hind Rajab was riding.\n**(7)**\nTwo Palestine Red Crescent paramedics attempting to rescue Hind Rajab in a marked ambulance along an approved route were also killed by Israeli tank fire as they approached the car.\n**(8)**\nForensic analysis determined the weapons and munitions used in the attacks were consistent with IDF-issued weaponry, including the M4 carbine assault rifle, the FN MAG machine gun on a Merkava battle tank, and 120mm M830A1 High Explosive Anti-Tank Multi-Purpose-Tracers, much of which is provided by, or includes components from, the United States.\n**(9)**\nForensic analysis and satellite imagery determined that an Israeli Merkava tank, which uses parts and components manufactured in the United States, was in proximity to the car on the day of the attack and consistent with the weapons used to kill Hind Rajab and her family.\n**(10)**\nOn April 16, 2024, a Department of State spokesperson said the Department would ask Israel for further information about the attacks and would welcome a full investigation into the matter.\n**(11)**\nSection 620M of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2378d ) prohibits the Secretary of State from providing assistance to any unit of a foreign security force if the Secretary has credible information that such unit has committed a gross violation of human rights. .\n#### 3. Prosecution of war crimes\n##### (a) Referral by Secretary of State\nNot later than 30 days after the date of the enactment of this Act, the Secretary of State shall certify to the appropriate congressional committees that if there is credible information indicating the attacks on January 29, 2024, which caused the deaths of Hind Rajab, members of her family, and 2 Palestine Red Crescent paramedics, could constitute war crimes and involved the use of United States-origin weapons or munitions, United States citizens, or IDF personnel trained by the United States, the Secretary will, not later than 15 days after such certification, refer such findings to the Attorney General for prosecution of those responsible for such attacks.\n##### (b) Investigation by Attorney General\nNot later than 30 days after the date of the enactment of this Act, the Attorney General shall certify to the appropriate congressional committees that the Department of Justice will\u2014\n**(1)**\nreview any referral received from the Secretary of State regarding the Gaza City attacks of January 29, 2024; and\n**(2)**\ninitiate an investigation and prosecutions for war crimes in accordance with section 2441 of title 18, United States Code, as appropriate, to the extent such actions fall within the jurisdiction of the United States courts.\n#### 4. Report on the Gaza City attacks on January 29, 2024\n##### (a) In general\nNot later than 45 days after the date of the enactment of this Act, the Secretary of State, in consultation with the Attorney General and the Secretary of War, shall submit a report to the appropriate congressional committees regarding the Gaza City attacks of January 29, 2024, as described in section 2.\n##### (b) Contents\nThe report submitted pursuant to subsection (a) shall include\u2014\n**(1)**\nall the information available to the United States Government regarding\u2014\n**(A)**\nthe identity of the IDF or other Israeli security force units that were involved in the attacks referred to in subsection (a);\n**(B)**\nthe underlying operational motivation for the attacks;\n**(C)**\nany actions taken by the Government of Israel to investigate the attacks and to hold accountable the individuals who were responsible for the attacks;\n**(D)**\nwhether any of the soldiers involved in the attacks were United States citizens;\n**(E)**\nwhether the IDF used any weapons or ammunition in the attacks that were provided by the United States; and\n**(F)**\nwhether any of the IDF personnel involved in the attacks were trained by the United States;\n**(2)**\nall actions taken by the Department of State to submit inquiries or requests for information to the Government of Israel regarding the attacks pursuant to the Department\u2019s formal acknowledgment of the attacks and commitment to seek such information;\n**(3)**\nall actions by the Department of State to request information from the intelligence community (as defined in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 )) and other components of the United States Government regarding the attacks;\n**(4)**\nthe extent to which the Secretary of State and the Secretary of War initiated an inquiry or investigation to determine if the attacks constituted a gross violation of human rights for purposes of mandatory compliance with section 620M of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2378d ) and section 362 of title 10, United States Code, respectively ( The Leahy Laws );\n**(5)**\nthe findings of any other Department of State reviews, policy recommendations, or internal investigations related to the attack, including actions taken under the Department of State\u2019s Civilian Harm Incident Response Guidance; and\n**(6)**\nwhether the Department of Justice\u2014\n**(A)**\nhas received information regarding the attacks;\n**(B)**\nhas relayed such information to the Human Rights and Special Prosecutions Section; and\n**(C)**\nhas established a record of such documents and the receipt of such information.\n#### 5. Compensation\nIt is the sense of Congress that\u2014\n**(1)**\nthe Government of Israel should provide compensation to the families of Hind Rajab and of the paramedics who were killed in the attacks on January 29, 2024; and\n**(2)**\nthe Department of State should also provide compensation to such families if it is determined that any United States citizens serving in the IDF were involved in the attacks.\n#### 6. Statement of policy\nIt shall be the policy of the United States\u2014\n**(1)**\nto collect, analyze, and preserve evidence and information relating to possible war crimes and atrocities committed during the Israel-Hamas war that began on October 7, 2023, for use in domestic, foreign, and international courts and tribunals prosecuting those responsible for such crimes, including evidence and information relating to the attacks on January 29, 2024, which caused the deaths of Hind Rajab, members of her family, and 2 Palestine Red Crescent paramedics;\n**(2)**\nto continue efforts to identify, deter, and pursue accountability for war crimes and other atrocities committed in conflicts around the world, including through the investigation and prosecution of crimes by the Department of Justice under section 2441 of title 18, United States Code (commonly known as the War Crimes Act of 1996 );\n**(3)**\nto consider the willful killing of protected persons, including civilians and medical personnel, as grave breaches amounting to war crimes and, if systemic, crimes against humanity;\n**(4)**\nto hold perpetrators of war crimes and crimes against humanity accountable for their crimes;\n**(5)**\nto uphold the Convention (IV) relative to the Protection of Civilian Persons in Time of War, done at Geneva August 12, 1949 (commonly referred to as the Fourth Geneva Convention ), to which the United States is party and has ratified, including article 3, which states that persons taking no active part in hostilities shall be treated humanely and should not be subject to violence to life and person;\n**(6)**\nto uphold article 35 of the Convention for the Amelioration of the Condition of the Wounded and Sick in Armed Forces in the Field, done at Geneva August 12, 1949, to which the United States is a party and has ratified, requires transports of wounded and sick or of medical equipment to be respected and protected in the same way as mobile medical units; and\n**(7)**\nfor the Attorney General, with input from the heads of other Federal agencies, as appropriate, to investigate any credible allegations of war crimes committed by United States citizens in Gaza, in accordance with section 2441 of title 18, United States Code.\n#### 7. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Armed Services of the Senate ;\n**(D)**\nthe Select Committee on Intelligence of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on the Judiciary of the House of Representatives ;\n**(G)**\nthe Committee on Armed Services of the House of Representatives ; and\n**(H)**\nthe Permanent Select Committee on Intelligence of the House of Representatives .\n**(2) Atrocities**\nThe term atrocities has the meaning given such term in section 6(2) of the Elie Wiesel Genocide and Atrocities Prevention Act of 2018 ( Public Law 115\u2013441 ; 22 U.S.C. 2656 note).\n**(3) War crime**\nThe term war crime has the meaning given such term in section 2441(c) of title 18, United States Code.",
      "versionDate": "2026-03-12",
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
        "actionDate": "2026-03-12",
        "text": "Read twice and referred to the Committee on Foreign Relations. (Sponsor introductory remarks on measure: CR S1049)"
      },
      "number": "4095",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Justice for Hind Rajab Act",
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
        "name": "International Affairs",
        "updateDate": "2026-03-27T22:02:41Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7903ih.xml"
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
      "title": "Justice for Hind Rajab Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T04:58:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Justice for Hind Rajab Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T04:58:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To call for accountability for the killing of innocent civilians, including 5-year-old Hind Rajab and 2 paramedics, in an attack in Gaza City on January 29, 2024, by Israel Defense Forces, to require the Secretary of State to report to Congress on the attack and to determine if any of the weapons and munitions used in the attack were provided by the United States or if any of the soldiers responsible for such killings were United States citizens or were trained by the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T04:48:28Z"
    }
  ]
}
```

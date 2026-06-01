# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4389?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4389
- Title: HELP Separated Children Act
- Congress: 119
- Bill type: S
- Bill number: 4389
- Origin chamber: Senate
- Introduced date: 2026-04-27
- Update date: 2026-05-19T21:56:52Z
- Update date including text: 2026-05-19T21:56:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in Senate
- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-27: Introduced in Senate

## Actions

- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4389",
    "number": "4389",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "HELP Separated Children Act",
    "type": "S",
    "updateDate": "2026-05-19T21:56:52Z",
    "updateDateIncludingText": "2026-05-19T21:56:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T21:12:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CT"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "WA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-04-27",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "VT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4389is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4389\nIN THE SENATE OF THE UNITED STATES\nApril 27, 2026 Ms. Smith (for herself, Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Ms. Cortez Masto , Ms. Duckworth , Mrs. Gillibrand , Ms. Hirono , Mr. Kaine , Mr. Kim , Ms. Klobuchar , Mr. Markey , Mrs. Murray , Ms. Rosen , Mr. Sanders , Ms. Warren , Mr. Welch , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo protect children affected by immigration enforcement actions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Humane Enforcement and Legal Protections for Separated Children Act or HELP Separated Children Act .\n#### 2. Definitions\nIn this Act:\n**(1) Apprehension**\nThe term apprehension means the detention or arrest by officials of the Department or cooperating entities.\n**(2) Child**\nThe term child means an individual who is younger than 18 years of age.\n**(3) Child welfare agency**\nThe term child welfare agency means a State or local agency responsible for child welfare services under subtitles B and E of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ).\n**(4) Cooperating entity**\nThe term cooperating entity means a Federal, State or local entity acting under an agreement with the Secretary relating to immigration detention and apprehension.\n**(5) Department**\nThe term Department means the Department of Homeland Security.\n**(6) Detention facility**\n**(A) In general**\nThe term detention facility means a Federal, State, or local government facility, or a privately owned and operated facility, that is used, in whole or in part, to hold individuals under the authority of the Director of U.S. Immigration and Customs Enforcement, including facilities that hold such individuals under a contract or agreement with the Director.\n**(B) Inclusions**\nThe term detention facility includes\u2014\n**(i)**\nany short-term holding facility operated by U.S. Immigration and Customs Enforcement or U.S. Customs and Border Protection that is used to hold individuals for internal immigration enforcement purposes; and\n**(ii)**\nany space where an individual or family unit is held in custody by the Department.\n**(7) Immigration enforcement action**\nThe term immigration enforcement action means the apprehension of 1 or more individuals who the Secretary has reason to believe are removable under section 237 of the Immigration and Nationality Act ( 8 U.S.C. 1227 ).\n**(8) Parent**\nThe term parent means\u2014\n**(A)**\na biological or adoptive parent of a child, or an adult otherwise recognized by the law of a foreign country as a parent, whose parental rights have not been relinquished or terminated under State law or the law of a foreign country;\n**(B)**\na legal guardian of a child under State law or the law of a foreign country; and\n**(C)**\na kin caregiver who has historically cared for a child when a parent is not present.\n**(9) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n#### 3. Identification of parents detained during immigration enforcement actions\nThe Secretary and any cooperating entity shall\u2014\n**(1)**\nas soon as practicable but generally not later than 2 hours after an immigration enforcement action occurs, inquire whether a detained or arrested individual is a parent of a child in the United States, and document such information; and\n**(2)**\ngenerally inquire about any changes to the parental status of the individual while the individual is in the custody of the Secretary or the cooperating entity\u2014\n**(A)**\nat every official interaction with personnel of a detention facility; and\n**(B)**\nnot less than 10 days before the date on which the individual is removed from the United States.\n#### 4. Apprehension procedures for immigration enforcement actions\n##### (a) In general\nIn any immigration enforcement action, the Secretary and any cooperating entity shall\u2014\n**(1)**\nprovide each apprehended individual who is a parent of a child in the United States\u2014\n**(A)**\nthe opportunity to make as many telephone calls as necessary to arrange for the care of such child in the absence of the individual; and\n**(B)**\nwith contact information, in the preferred language of the individual, for\u2014\n**(i)**\nattorneys and legal service providers capable of providing free legal advice or representation regarding child welfare, child custody determinations, and immigration matters;\n**(ii)**\nthe consulate of the applicable foreign country; and\n**(iii)**\nchild welfare agencies and family courts in the jurisdiction in which any such child is located;\n**(2)**\nnotify the child welfare agency with jurisdiction over any such child only if\u2014\n**(A)**\nthe apprehended parent wants the child to remain in the United States and is unable to make care arrangements for the child; or\n**(B)**\nthe Department has information specific to any such child that the child is at imminent risk of serious harm, and any such information shall be documented and shared with the apprehended parent;\n**(3)**\nexcept in a case of medical necessity or in extraordinary circumstances, ensure that personnel of the Department and the cooperating entity do not\u2014\n**(A)**\nin the presence of any child, make excessive use of force, including drawing weapons and throwing individuals to the ground, in the arrest or apprehension of individuals;\n**(B)**\ncompel or request any child to interpret or translate in the interview of a parent or of any other individual encountered during the immigration enforcement action; or\n**(C)**\nengage in any deception of a child for purposes of facilitating or initiating immigrant enforcement against the child\u2019s parents, other family or household members, or any other individual;\n**(4)**\nin the case of an apprehended parent whose child is present during the immigration enforcement action, except in extraordinary circumstances, ensure that the parent is provided an opportunity\u2014\n**(A)**\nto communicate with the child, including through physical contact;\n**(B)**\nto reassure the child; and\n**(C)**\nto share information regarding care arrangements for the child with any other individual who is present or who may be reached by telephone while the apprehended parent is detained; and\n**(5)**\nensure that any apprehended individual who is a parent of a child in the United States\u2014\n**(A)**\nexcept in a case of medical necessity or in extraordinary circumstances\u2014\n**(i)**\nis not transferred from the location at which the individual is apprehended until the individual\u2014\n**(I)**\nhas made arrangements for the care of such child; or\n**(II)**\nif such arrangements are unavailable or the individual is unable to make such arrangements within 48 hours of the immigration enforcement action\u2014\n**(aa)**\nis consulted and allowed to participate in the decisionmaking process to arrange with the Department for the care arrangements made for the child; and\n**(bb)**\nis provided with a means to maintain communication with the child; and\n**(ii)**\nto the extent practicable, is placed in a detention facility that will facilitate opportunities for regular visitation with a child during detention and is proximate to\u2014\n**(I)**\nthe habitual place of residence of the child; and\n**(II)**\nthe location of the immigration enforcement action; and\n**(B)**\nreceives due consideration of the best interests of the child in any decision or action relating to the individual's detention, release, or transfer between detention facilities.\n##### (b) Requests to State and local entities\nIf the Secretary makes a request to a cooperating entity to hold in custody an individual who the Secretary has reason to believe is removable under section 237 of the Immigration and Nationality Act ( 8 U.S.C. 1227 ) pending transfer of such individual to the custody of the Secretary or to a detention facility, the Secretary shall ensure that the cooperating entity provides the individual the protections described in paragraphs (1) and (2) of subsection (a) if such individual is the parent of a child in the United States.\n##### (c) Protections against trafficking preserved\nNothing in this section may be construed to impede, delay, or limit the obligations of the Secretary, the Attorney General, or the Secretary of Health and Human Services under\u2014\n**(1)**\nsection 235 of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232 );\n**(2)**\nsection 462 of the Homeland Security Act of 2002 ( 6 U.S.C. 279 ); or\n**(3)**\nthe Stipulated Settlement Agreement filed in the United States District Court for the Central District of California on January 17, 1997 (CV 85\u20134544\u2013RJK) (commonly known as the Flores Settlement Agreement ).\n#### 5. Access to children, State and local courts, child welfare agencies, and consular officials\n##### (a) In general\nAt each detention facility, the Secretary shall\u2014\n**(1)**\nprominently post, in a manner accessible to detainees and visitors, and include in detainee handbooks\u2014\n**(A)**\ninformation regarding the protections under this Act; and\n**(B)**\ninformation regarding potential eligibility for parole or release;\n**(2)**\nexcept in extraordinary circumstances, ensure that each individual detained by the Department who is a parent of a child in the United States\u2014\n**(A)**\nhas the opportunity to make free, regular phone and video calls and contact visits with such child, ideally in a community or child-friendly setting;\n**(B)**\nis provided with contact information for child welfare agencies and family courts in the relevant jurisdictions;\n**(C)**\nhas the opportunity to participate fully and, to the extent practicable, in person\u2014\n**(i)**\nin all family court proceedings;\n**(ii)**\nin any other proceeding that may impact the right of the individual to custody of such child; and\n**(iii)**\nin case planning activities;\n**(D)**\nhas the opportunity to make free and confidential telephone calls to legal counsel, relevant child welfare agencies, and family courts as often as necessary to ensure that the best interests of such child, including a preference for family unity whenever appropriate, may be considered in child welfare agency or family court proceedings; and\n**(E)**\nis provided\u2014\n**(i)**\nthe opportunity to fully comply with all family court or child welfare agency orders impacting the custody of such child;\n**(ii)**\naccess to United States passport applications or other relevant travel document applications for the purpose of obtaining travel documents for such child;\n**(iii)**\ntimely access to a notary public for purposes of applying for a passport for such child or executing guardianship or other agreements to ensure the safety of such child; and\n**(iv)**\nadequate time and opportunity before removal to obtain passports, apostilled birth certificates, travel documents, medical records, educational records, and other necessary records on behalf of such child if such child will accompany the individual to the country of origin of the individual or eventually join the individual in such country; and\n**(3)**\nif doing so would not impact public safety or national security, facilitate the ability of each detained parent to share information regarding travel arrangements with his or her counsel, consulate, children, child welfare agencies, or other caregivers before the parent departs the United States.\n##### (b) Designation of points of contact\nFor each detention facility and field office of U.S. Immigration and Customs Enforcement, the Secretary shall designate a point of contact who shall be responsible for ensuring that each detained parent of a child who is in the United States is provided all opportunities necessary to comply with child welfare case plans and participate in family court proceedings.\n##### (c) Appointment of national coordinator\nThe Secretary shall appoint a national coordinator who shall\u2014\n**(1)**\nserve as the primary point of contact and subject-matter expert for all U.S. Immigration and Customs Enforcement personnel regarding State child welfare and guardianship issues for parents subject to immigration enforcement actions;\n**(2)**\nconduct data collection and analysis with respect to the parental status of individuals who are in the custody of the Secretary;\n**(3)**\non an ongoing basis, share relevant information based on such data with points of contact designated under subsection (b);\n**(4)**\nprovide child welfare stakeholders and such points of contact with guidance and training on\u2014\n**(A)**\nfacilitating the ability of detained parents to participate in family court proceedings relating to their children;\n**(B)**\nvisitation protocols; and\n**(C)**\ncoordinating contact between parents and counsel, consulates, child welfare personnel, family members, and caregivers; and\n**(5)**\nfacilitate reunification with parents prior to removal and after removal if requested by the parent, including by\u2014\n**(A)**\nestablishing procedures;\n**(B)**\nassisting with travel documents;\n**(C)**\ncoordinating with Federal, State, and local child welfare agencies, caretakers, foreign governments, and other appropriate stakeholders; and\n**(D)**\narranging travel.\n#### 6. Prosecutorial discretion\nThe Secretary shall prioritize the exercise of discretion in any instance in which the parent of a child is subject to an immigration enforcement action by considering the best interests of the child in decisions, including\u2014\n**(1)**\nwhether to prosecute the individual for 1 or more immigration violations;\n**(2)**\nwhether to transfer the individual to another detention facility that is farther away from the place of habitual residence of the child;\n**(3)**\nwhether to release the individual so the individual may continue to care for the child; and\n**(4)**\nwhether to consider alternatives to the detention or release of the individual.\n#### 7. Facilitation of return to the United States\nThe Secretary may facilitate on a case-by-case basis reentry of a parent to the United States who was previously removed through a grant of parole if the individual is able to demonstrate\u2014\n**(1)**\nthat the individual has a termination of parental rights hearing or other family court hearing pending or ongoing in the United States for the purposes of attending the hearing;\n**(2)**\nthat the child of the individual is experiencing a humanitarian need, such as a medical emergency; or\n**(3)**\nthat the child of the individual is deceased for purposes of attending the funeral of the child in the United States.\n#### 8. Mandatory training\n##### (a) In general\nThe Secretary, in consultation with the Secretary of Health and Human Services and independent child welfare and family law experts, shall develop and provide training on the protections required under sections 4 and 5 (including on methods to minimize trauma to children and to detect signs of abuse or neglect) to all employees of the Department, cooperating entities, and detention facilities who\u2014\n**(1)**\nhold positions related to parental interests;\n**(2)**\nregularly engage in immigration enforcement actions, including the detention of individuals; and\n**(3)**\nin the course of such actions, come into contact with parents of children who are in the United States.\n##### (b) Provision of training\nThe training under subsection (a) shall be provided\u2014\n**(1)**\nin the case of current employees of the Department, cooperating entities, and detention facilities, not later than 180 days after the date of the enactment of this Act, and annually thereafter; and\n**(2)**\nin the case of any employee of the Department, a cooperating entity, or a detention facility who is hired after the date that is 180 days after the date of the enactment of this Act, on the date on which the employee commences duty, and annually thereafter.\n#### 9. Data collection\n##### (a) In general\nOn the date that is 180 days after the date of the enactment of this Act, and every 180 days thereafter, the Secretary, in consultation and collaboration with the Secretary of Health and Human Services, shall collect and maintain the following information:\n**(1)**\nOf individuals in the custody of U.S. Immigration and Customs Enforcement\u2014\n**(A)**\nthe number and percentage who are parents of a child who is in the United States; and\n**(B)**\nthe number and percentage who are parents of a child involved in the child welfare system in the United States.\n**(2)**\nFor the preceding 180-day period\u2014\n**(A)**\nthe number of parents of a child in the United States who have been apprehended by U.S. Immigration and Customs Enforcement and released; and\n**(B)**\nof the number of individuals released by U.S. Immigration and Customs Enforcement during such period, the percentage who are such parents.\n**(3)**\nThe number of individuals in the custody of U.S. Immigration and Customs Enforcement who are parents of a child involved in the child welfare system in the United States, and the percentage of such individuals among all individuals detained by U.S. Immigration and Customs Enforcement who are parents.\n**(4)**\nThe number of individuals who are parents of a child involved in the child welfare system in the United States who have been released from the custody of U.S. Immigration and Customs Enforcement, and the percentage of such individuals among all individuals who are parents and have been released from the custody of U.S. Immigration and Customs Enforcement.\n**(5)**\nThe number of parents subject to a final order of removal who have elected to take their child with them to the country of removal, and the percentage of such parents among all parents with children who are subject to removal orders.\n**(6)**\nThe number of parents subject to a final order of removal who have elected to leave their child in the United States, and the percentage of such parents among all parents with children who are subject to removal orders.\n**(7)**\nThe number of personnel who have received training on the parental rights of individuals in the custody of U.S. Immigration and Customs Enforcement, the titles of such personnel, and the percentage of such personnel among all field staff of U.S. Immigration and Customs Enforcement.\n**(8)**\nThe average number of visits a detained parent receives from his or her child during a 180-day period.\n**(9)**\nThe average and median distance between a detention facility housing detainee parents and the domicile of the children of such parents.\n**(10)**\nThe number of transfers, if any, to different detention facilities a parent experienced, including the distance of the facility from the site of the enforcement action.\n##### (b) Report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, the Secretary shall submit a report that contains the information collected under subsection (a) for the preceding 180-day period to\u2014\n**(A)**\nthe Committee on the Judiciary, the Committee on Homeland Security and Governmental Affairs, and the Committee on Health, Education, Labor, and Pensions of the Senate; and\n**(B)**\nthe Committee on the Judiciary, the Committee on Homeland Security, and the Committee on Education and Workforce of the House of Representatives.\n**(2) Initial report**\nThe initial report submitted under paragraph (1) shall include a detailed summary of the initial efforts of the Secretary to fulfill the obligations under this Act, including a description of the manner in which the Secretary plans to establish or integrate data collection and storage protocols related to this Act.\n**(3) Subsequent reports**\nEach subsequent report submitted under paragraph (1) shall include\u2014\n**(A)**\nthe number of employees of the Department, coordinating entities, and detention facilities provided annual training under section 7; and\n**(B)**\nthe number of new employees of the Department, coordinating entities, and detention facilities who have been provided an initial training under that section.\n##### (c) Public availability\nThe Secretary shall make the report required by subsection (b) available to the public on a website of the Department.\n##### (d) Methods\nIn carrying out this section, the Secretary shall ensure that\u2014\n**(1)**\nthe methods for collecting information are consistent from year to year so as to enable the tracking of trends across years; and\n**(2)**\npersonally identifiable information is protected.\n#### 10. Rulemaking\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall promulgate regulations to implement this Act.\n#### 11. Severability\nIf any provision of this Act, any amendment made by this Act, or the application of any such provision or amendment to any person or circumstance is held to be unconstitutional, the remaining provisions of this Act, the remaining amendments made by this Act, and the application of such provisions and amendments to any person or circumstance shall not be affected by such holding.",
      "versionDate": "2026-04-27",
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
        "name": "Immigration",
        "updateDate": "2026-05-19T21:56:52Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4389is.xml"
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
      "title": "HELP Separated Children Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HELP Separated Children Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Humane Enforcement and Legal Protections for Separated Children Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect children affected by immigration enforcement actions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:29Z"
    }
  ]
}
```

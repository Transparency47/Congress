# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3527
- Title: Real Education and Access for Healthy Youth Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3527
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-05-14T08:07:55Z
- Update date including text: 2026-05-14T08:07:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-21 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-21 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3527",
    "number": "3527",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000370",
        "district": "12",
        "firstName": "Alma",
        "fullName": "Rep. Adams, Alma S. [D-NC-12]",
        "lastName": "Adams",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Real Education and Access for Healthy Youth Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:55Z",
    "updateDateIncludingText": "2026-05-14T08:07:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-21T14:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "WA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "VA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "IL"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "OR"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "IL"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "FL"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "WA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "WA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "OH"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "DC"
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
      "sponsorshipDate": "2025-06-05",
      "state": "AL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "PA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "IL"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NC"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "WI"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MI"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sponsorshipDate": "2026-05-13",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3527ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3527\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Ms. Adams (for herself, Ms. Jayapal , Mr. Beyer , Mr. Davis of Illinois , and Ms. Bonamici ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for the overall health and well-being of young people, including the promotion and attainment of lifelong sexual health and healthy relationships, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Real Education and Access for Healthy Youth Act of 2025 .\n#### 2. Purpose and findings\n##### (a) Purpose\nThe purpose of this Act is to provide young people with sex education and sexual health services that\u2014\n**(1)**\npromote and uphold the rights of young people to information and services that empower them to make decisions about their bodies, health, sexuality, families, and communities in all areas of life;\n**(2)**\nare evidence-informed, comprehensive in scope, confidential, equitable, accessible, medically accurate and complete, age and developmentally appropriate, culturally responsive, trauma-informed and resilience-oriented, and align with the National Sex Education Standards of the Future of Sex Ed Initiative;\n**(3)**\nprovide information about the prevention, treatment, and care of pregnancy, sexually transmitted infections, and interpersonal violence;\n**(4)**\nprovide information about the importance of consent as a basis for healthy relationships and for autonomy in health care;\n**(5)**\nprovide information on gender identity and gender expression;\n**(6)**\nprovide information on the historical and current condition in which education and health systems, policies, programs, services, and practices have uniquely and adversely impacted Black, Indigenous, Latine, Asian American, Native Hawaiian, Pacific Islander, and other People of Color; and\n**(7)**\nredress inequities in the delivery of sex education and sexual health services to underserved young people.\n##### (b) Findings\nCongress finds the following:\n**(1)**\nYoung people need and have the right to sex education and sexual health services that are evidence-informed, comprehensive in scope, confidential, equitable, accessible, medically accurate and complete, age and developmentally appropriate, culturally responsive, and trauma-informed and resilience-oriented.\n**(2)**\nCurrently, there is a gap between the sex education that young people should be receiving based on expert standards and the sex education many actually receive.\n**(3)**\nOnly 36 States and the District of Columbia mandate sex education or human immunodeficiency virus (HIV) education in schools.\n**(4)**\nWhen there is sex education or instruction regarding HIV or sexually transmitted infections (STI), 13 States do not require the content to be evidence-informed, medically accurate and complete, age and developmentally appropriate, or culturally responsive.\n**(5)**\nMany sex education programs and sexual health services currently available were not designed to and do not currently meet the needs of underserved young people. Some such programs and services actually harm underserved young people.\n**(6)**\nFor underserved young people, a lack of comprehensive in scope, confidential, equitable, and accessible sex education and sexual health services is not unfamiliar, but rather a longstanding manifestation of white supremacy, which has touched every aspect of our history, culture, and institutions, including the education and health care systems.\n**(7)**\nThe development and delivery of sexual health education and sexual health services in the United States historically has been rooted in the oppression of Black, Indigenous, Latine, Asian American, Native Hawaiian, Pacific Islander, and other People of Color.\n**(8)**\nThe United States has a long history of eugenics and forced sterilization. The sexual and reproductive rights and bodily autonomy of specific communities deemed undesirable or defective were targeted by our governments resulting in state-sanctioned violence and generations of trauma and oppression. These communities include\u2014\n**(A)**\npeople with low incomes;\n**(B)**\nimmigrants;\n**(C)**\npeople with disabilities;\n**(D)**\npeople living with HIV;\n**(E)**\nsurvivors of interpersonal violence;\n**(F)**\npeople who are incarcerated, detained, or who otherwise have encountered the criminal-legal system;\n**(G)**\nBlack, Indigenous, Latine, Asian American, and other People of Color;\n**(H)**\npeople who are lesbian, gay, bisexual, transgender, and queer; and\n**(I)**\nyoung people who are pregnant and parenting.\n**(9)**\nBlack young people are more likely to receive abstinence-only instruction. Research shows that abstinence-only instruction, also known as sexual risk avoidance instruction, is ineffective in comparison to comprehensive sex education.\n**(10)**\nBlack, Indigenous, and Latine young people are disproportionately more likely to be diagnosed with an STI, have an unintended pregnancy, or experience sexual assault.\n**(11)**\nThe framework of Reproductive Justice acknowledges and aims to address the legacy of white supremacy, systemic oppression, and the restrictions on sex education and sexual health services that disproportionately impact underserved communities. Reproductive Justice will be achieved when all people regardless of actual or perceived race, color, ethnicity, national origin, religion, immigration status, sex (including gender identity and sexual orientation), disability status, pregnancy or parenting status, or age have the power to make decisions about their bodies, health, sexuality, families, and communities in all areas of life.\n**(12)**\nIncreased resources are required for sex education and sexual health services to reach all young people, redress inequities and their impacts on underserved young people, and achieve Reproductive Justice for young people.\n**(13)**\nSuch sex education and sexual health services should\u2014\n**(A)**\npromote and uphold the rights of young people to information and services in order to make and exercise informed and responsible decisions about their sexual health;\n**(B)**\nbe evidence-informed, comprehensive in scope, confidential, equitable, accessible, age and developmentally appropriate, culturally responsive, and trauma-informed and resilience-oriented;\n**(C)**\ninclude instruction and materials that address\u2014\n**(i)**\npuberty and adolescent development;\n**(ii)**\nsexual and reproductive anatomy and physiology;\n**(iii)**\nsexual orientation, gender identity, and gender expression;\n**(iv)**\ncontraception, pregnancy, and reproduction;\n**(v)**\nHIV and other STIs;\n**(vi)**\nconsent and healthy relationships; and\n**(vii)**\ninterpersonal violence;\n**(D)**\npromote gender equity and be inclusive of young people with varying gender identities, gender expressions, and sexual orientations;\n**(E)**\npromote safe and healthy relationships; and\n**(F)**\npromote racial equity and be responsive to the needs of young people who are Black, Indigenous, and other People of Color.\n#### 3. Definitions\nIn this Act:\n**(1) Age and developmentally appropriate**\nThe term age and developmentally appropriate means topics, messages, and teaching methods suitable to particular ages, age groups, or developmental levels, based on cognitive, emotional, social, and behavioral capacity of most young people at that age level.\n**(2) Consent**\nThe term consent means affirmative, conscious, and voluntary agreement to engage in interpersonal, physical, or sexual activity.\n**(3) Culturally responsive**\nThe term culturally responsive means education and services that\u2014\n**(A)**\nembrace and actively engage and adjust to young people and their various cultural identities;\n**(B)**\nrecognize the ways in which many underserved young people face unique barriers in our society that result in increased adverse health outcomes and associated stereotypes; and\n**(C)**\nmay address the ways in which racism has shaped national health care policy, the lasting historical trauma associated with reproductive health experiments and forced sterilizations of Black, Latine, and Indigenous communities, or sexual stereotypes assigned to young People of Color or LGBTQ+ people.\n**(4) Evidence-informed**\nThe term evidence-informed means incorporating characteristics, content, or skills that have been proven to be effective through evaluation in changing sexual behavior.\n**(5) Gender expression**\nThe term gender expression means the expression of one\u2019s gender, such as through behavior, clothing, haircut, or voice, and which may or may not conform to socially defined behaviors and characteristics typically associated with being either masculine or feminine.\n**(6) Gender identity**\nThe term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual\u2019s designated sex at birth.\n**(7) Inclusive**\nThe term inclusive means content and skills that ensure underserved young people are valued, respected, centered, and supported in sex education instruction and materials.\n**(8) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(9) Interpersonal violence**\nThe term interpersonal violence means abuse, assault, bullying, dating violence, domestic violence, harassment, intimate partner violence, or stalking.\n**(10) Local educational agency**\nThe term local educational agency has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(11) Medically accurate and complete**\nThe term medically accurate and complete means that\u2014\n**(A)**\nthe information provided through the education is verified or supported by the weight of research conducted in compliance with accepted scientific methods and is published in peer-reviewed journals, where applicable; or\n**(B)**\nthe education contains information that leading professional organizations and agencies with relevant expertise in the field recognize as accurate, objective, and complete.\n**(12) Resilience**\nThe term resilience means the ability to adapt to trauma and tragedy.\n**(13) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(14) Sex education**\nThe term sex education means high quality teaching and learning that\u2014\n**(A)**\nis delivered, to the maximum extent practicable, following the National Sexuality Education Standards of the Future of Sex Ed Initiative;\n**(B)**\nis about a broad variety of topics related to sex and sexuality, including\u2014\n**(i)**\npuberty and adolescent development;\n**(ii)**\nsexual and reproductive anatomy and physiology;\n**(iii)**\nsexual orientation, gender identity, and gender expression;\n**(iv)**\ncontraception, pregnancy, pregnancy options, and reproduction;\n**(v)**\nHIV and other STIs;\n**(vi)**\nconsent and healthy relationships; and\n**(vii)**\ninterpersonal violence;\n**(C)**\nexplores values and beliefs about such topics; and\n**(D)**\nhelps young people in gaining the skills that are needed to navigate relationships and manage one\u2019s own sexual health.\n**(15) Sexual health services**\nThe term sexual health services includes\u2014\n**(A)**\nsexual health information, education, and counseling;\n**(B)**\nall methods of contraception approved by the Food and Drug Administration;\n**(C)**\nroutine gynecological care, including human papillomavirus (HPV) vaccines and cancer screenings;\n**(D)**\npre-exposure prophylaxis or post-exposure prophylaxis;\n**(E)**\nsubstance use and mental health services;\n**(F)**\ninterpersonal violence survivor services; and\n**(G)**\nother pregnancy and STI prevention, care, or treatment services.\n**(16) Sexual orientation**\nThe term sexual orientation means an individual\u2019s romantic, emotional, or sexual attraction to other people.\n**(17) State educational agency**\nThe term State educational agency has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(18) Trauma**\nThe term trauma means a response to an event, series of events, or set of circumstances that is experienced or witnessed by an individual or group of people as physically or emotionally harmful or life-threatening with lasting adverse effects on their functioning and mental, physical, social, emotional, or spiritual well-being.\n**(19) Trauma-informed and resilience-oriented**\nThe term trauma-informed and resilience-oriented means an approach that realizes the prevalence of trauma, recognizes the various ways individuals, organizations, and communities may respond to trauma differently, recognizes that resilience can be built, and responds by putting this knowledge into practice.\n**(20) Underserved young people**\nThe term underserved young people means young people who are disadvantaged by underlying structural barriers and social inequities, including young people who are\u2014\n**(A)**\nBlack, Indigenous, Latine, Asian American, Native Hawaiian, Pacific Islander, and other People of Color;\n**(B)**\nimmigrants;\n**(C)**\nin contact with the foster care system;\n**(D)**\nin contact with the juvenile justice system;\n**(E)**\nexperiencing homelessness;\n**(F)**\npregnant or parenting;\n**(G)**\nlesbian, gay, bisexual, transgender, or queer;\n**(H)**\nliving with HIV;\n**(I)**\nliving with disabilities;\n**(J)**\nfrom families with low-incomes; or\n**(K)**\nliving in rural areas.\n**(21) Young people**\nThe term young people means individuals who are ages 10 through 29 at the time of commencement of participation in a project supported under this Act.\n**(22) Youth-friendly sexual health services**\nThe term youth-friendly sexual health services means sexual health services that are provided in a confidential, equitable, and accessible manner that makes it easy and comfortable for young people to seek out and receive services.\n#### 4. Grants for sex education at elementary and secondary schools and youth-serving organizations\n##### (a) Program authorized\nThe Secretary, in coordination with the Secretary of Education, shall award grants, on a competitive basis, to eligible entities to enable such eligible entities to carry out projects that provide young people with sex education.\n##### (b) Duration\nGrants awarded under this section shall be for a period of 5 years.\n##### (c) Eligible entity\nIn this section, the term eligible entity means a public or private entity that delivers health education to young people.\n##### (d) Applications\nAn eligible entity desiring a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n##### (e) Priority\nIn awarding grants under this section, the Secretary shall give priority to eligible entities that are\u2014\n**(1)**\nState educational agencies or local educational agencies; or\n**(2)**\nIndian Tribes or Tribal organizations, as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n##### (f) Use of funds\nEach eligible entity that receives a grant under this section shall use the grant funds to carry out a project that provides young people with sex education.\n#### 5. Grants for sex education at institutions of higher education\n##### (a) Program authorized\nThe Secretary, in coordination with the Secretary of Education, shall award grants, on a competitive basis, to institutions of higher education or consortia of such institutions to enable such institutions to provide students with age and developmentally appropriate sex education.\n##### (b) Duration\nGrants awarded under this section shall be for a period of 5 years.\n##### (c) Applications\nAn institution of higher education or consortium of such institutions desiring a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n##### (d) Priority\nIn awarding grants under this section, the Secretary shall give priority to an institution of higher education that\u2014\n**(1)**\nhas an enrollment of needy students, as defined in section 318(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059e(b) );\n**(2)**\nis a Hispanic-serving institution, as defined in section 502(a) of such Act ( 20 U.S.C. 1101a(a) );\n**(3)**\nis a Tribal College or University, as defined in section 316(b) of such Act ( 20 U.S.C. 1059c(b) );\n**(4)**\nis an Alaska Native-serving institution, as defined in section 317(b) of such Act ( 20 U.S.C. 1059d(b) );\n**(5)**\nis a Native Hawaiian-serving institution, as defined in section 317(b) of such Act ( 20 U.S.C. 1059d(b) );\n**(6)**\nis a Predominantly Black Institution, as defined in section 318(b) of such Act ( 20 U.S.C. 1059e(b) );\n**(7)**\nis a Native American-serving, nontribal institution, as defined in section 319(b) of such Act ( 20 U.S.C. 1059f(b) );\n**(8)**\nis an Asian American and Native American Pacific Islander-serving institution, as defined in section 320(b) of such Act ( 20 U.S.C. 1059g(b) ); or\n**(9)**\nis a minority institution, as defined in section 365 of such Act ( 20 U.S.C. 1067k ), with an enrollment of needy students, as defined in section 312 of such Act ( 20 U.S.C. 1058 ).\n##### (e) Uses of funds\nAn institution of higher education or consortium of such institutions receiving a grant under this section shall use grant funds to develop and implement a project to integrate sex education into the institution of higher education in order to reach a large number of students, by carrying out 1 or more of the following activities:\n**(1)**\nAdopting and incorporating age and developmentally appropriate sex education into student orientation, general education, or courses.\n**(2)**\nDeveloping or adopting and implementing educational programming outside of class that delivers age and developmentally appropriate sex education to students.\n**(3)**\nDeveloping or adopting and implementing innovative technology-based approaches to deliver age and developmentally appropriate sex education to students.\n**(4)**\nDeveloping or adopting and implementing peer-led activities to generate discussion, educate, and raise awareness among students about age and developmentally appropriate sex education.\n**(5)**\nDeveloping or adopting and implementing policies and practices to link students to sexual health services.\n#### 6. Grants for educator training\n##### (a) Program authorized\nThe Secretary, in coordination with the Secretary of Education, shall award grants, on a competitive basis, to eligible entities to enable such eligible entities to carry out the activities described in subsection (e).\n##### (b) Duration\nGrants awarded under this section shall be for a period of 5 years.\n##### (c) Eligible entity\nIn this section, the term eligible entity means\u2014\n**(1)**\na State educational agency or local educational agency;\n**(2)**\nan Indian Tribe or Tribal organization, as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 );\n**(3)**\na State or local department of health;\n**(4)**\nan educational service agency, as defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 );\n**(5)**\na nonprofit institution of higher education or a consortium of such institutions; or\n**(6)**\na national or statewide nonprofit organization or consortium of nonprofit organizations that has as its primary purpose the improvement of provision of sex education through training and effective teaching of sex education.\n##### (d) Application\nAn eligible entity desiring a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n##### (e) Authorized activities\n**(1) Required activity**\nEach eligible entity receiving a grant under this section shall use grant funds for professional development and training of relevant teachers, health educators, faculty, administrators, and staff, in order to increase effective teaching of sex education to young people.\n**(2) Permissible activities**\nEach eligible entity receiving a grant under this section may use grant funds to\u2014\n**(A)**\nprovide training and support for educators about the content, skills, and professional disposition needed to implement sex education effectively;\n**(B)**\ndevelop and provide training and support to educators on incorporating anti-racist and gender inclusive policies and practices in sex education;\n**(C)**\nsupport the dissemination of information on effective practices and research findings concerning the teaching of sex education;\n**(D)**\nsupport research on\u2014\n**(i)**\neffective sex education teaching practices; and\n**(ii)**\nthe development of assessment instruments and strategies to document\u2014\n**(I)**\nyoung people\u2019s understanding of sex education; and\n**(II)**\nthe effects of sex education;\n**(E)**\nconvene conferences on sex education, in order to effectively train educators in the provision of sex education; and\n**(F)**\ndevelop and disseminate appropriate research-based materials to foster sex education.\n**(3) Subgrants**\nEach eligible entity receiving a grant under this section may award subgrants to nonprofit organizations that possess a demonstrated record of providing training to teachers, health educators, faculty, administrators, and staff on sex education to\u2014\n**(A)**\ntrain educators in sex education;\n**(B)**\nsupport internet or distance learning related to sex education;\n**(C)**\npromote rigorous academic standards and assessment techniques to guide and measure student performance in sex education;\n**(D)**\nencourage replication of best practices and model programs to promote sex education;\n**(E)**\ndevelop and disseminate effective, research-based sex education learning materials in multiple languages; or\n**(F)**\ndevelop academic courses on the pedagogy of sex education at institutions of higher education.\n#### 7. Authorization of grants to support the delivery of sexual health services to underserved young people\n##### (a) Program authorized\nThe Secretary shall award grants, on a competitive basis, to eligible entities to enable such entities to provide youth-friendly sexual health services to underserved young people.\n##### (b) Duration\nGrants awarded under this section shall be for a period of 5 years.\n##### (c) Eligible entity\nIn this section, the term eligible entity means\u2014\n**(1)**\na public or private youth-serving organization; or\n**(2)**\na covered entity, as defined in section 340B of the Public Health Service Act ( 42 U.S.C. 256b ).\n##### (d) Applications\nAn eligible entity desiring a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n##### (e) Uses of funds\nEach eligible entity that receives a grant under this section may use the grant funds to\u2014\n**(1)**\ndevelop and implement an evidence-informed project to deliver sexual health services to underserved young people;\n**(2)**\nestablish, alter, or modify staff positions, service delivery policies and practices, service delivery locations, service delivery environments, service delivery schedules, or other services components in order to increase youth-friendly sexual health services to underserved young people;\n**(3)**\nconduct outreach to underserved young people to invite them to participate in the eligible entity\u2019s sexual health services and to provide feedback to inform improvements in the delivery of such services;\n**(4)**\nestablish and refine systems of referral to connect underserved young people to other sexual health services and supportive services;\n**(5)**\nestablish partnerships and collaborations with entities providing services to underserved young people to link such young people to sexual health services, such as by delivering health services at locations where they congregate, providing transportation to locations where sexual health services are provided, or other linkages to services approaches;\n**(6)**\nprovide evidence-informed, comprehensive in scope, confidential, equitable, accessible, medically accurate and complete, age and developmentally appropriate, culturally responsive, and trauma-informed and resilience-oriented sexual health information to underserved young people in the languages and cultural contexts that are most appropriate for the underserved young people to be served by the eligible entity;\n**(7)**\npromote effective communication regarding sexual health among underserved young people; and\n**(8)**\nprovide training and support for eligible entity personnel and community members who work with underserved young people about the content, skills, and professional disposition needed to provide youth-friendly sex education and youth-friendly sexual health services.\n#### 8. Reporting and impact evaluation\n##### (a) Grantee report to secretary\nFor each year a grantee receives grant funds under section 4, 5, 6, or 7, the grantee shall submit to the Secretary a report that includes\u2014\n**(1)**\nthe use of grant funds by the grantee;\n**(2)**\nhow the use of grant funds has increased the access of young people to sex education or sexual health services; and\n**(3)**\nsuch other information as the Secretary may require.\n##### (b) Secretary\u2019s report to Congress\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter for a period of 5 years, the Secretary shall prepare and submit to Congress a report on the activities funded under this Act. The Secretary\u2019s report to Congress shall include\u2014\n**(1)**\na statement of how grants awarded by the Secretary meet the purpose described in section 2(a); and\n**(2)**\ninformation about\u2014\n**(A)**\nthe number of grantees that are receiving grant funds under sections 4, 5, 6, and 7;\n**(B)**\nthe specific activities supported by grant funds awarded under sections 4, 5, 6, and 7;\n**(C)**\nthe number of young people served by projects funded under sections 4, 5, and 7, in the aggregate and disaggregated and cross-tabulated by grant program, race and ethnicity, sex, sexual orientation, gender identity, and other characteristics determined by the Secretary (except that such disaggregation or cross-tabulation shall not be required in a case in which the results would reveal personally identifiable information about an individual young person);\n**(D)**\nthe number of teachers, health educators, faculty, school administrators, and staff trained under section 6; and\n**(E)**\nthe status of the evaluation required under subsection (c).\n##### (c) Multi-Year evaluation\n**(1) In general**\nNot later than 6 months after the date of the enactment of this Act, the Secretary shall enter into a contract with a nonprofit organization with experience in conducting impact evaluations to conduct a multi-year evaluation on the impact of the projects funded under sections 4, 5, 6, and 7 and to report to Congress and the Secretary on the findings of such evaluation.\n**(2) Evaluation**\nThe evaluation conducted under this subsection shall\u2014\n**(A)**\nbe conducted in a manner consistent with relevant, nationally recognized professional and technical evaluation standards;\n**(B)**\nuse sound statistical methods and techniques relating to the behavioral sciences, including quasi-experimental designs, inferential statistics, and other methodologies and techniques that allow for conclusions to be reached;\n**(C)**\nbe carried out by an independent organization that has not received a grant under section 4, 5, 6, or 7; and\n**(D)**\nbe designed to provide information on output measures and outcome measures to be determined by the Secretary.\n**(3) Report**\nNot later than 6 years after the date of enactment of this Act, the organization conducting the evaluation under this subsection shall prepare and submit to the appropriate committees of Congress and the Secretary an evaluation report. Such report shall be made publicly available, including on the website of the Department of Health and Human Services.\n#### 9. Nondiscrimination\nActivities funded under this Act shall not discriminate on the basis of actual or perceived sex (including sexual orientation and gender identity), age, parental status, race, color, ethnicity, national origin, disability, or religion. Nothing in this Act shall be construed to invalidate or limit rights, remedies, procedures, or legal standards available under any other Federal law or any law of a State or a political subdivision of a State, including the Civil Rights Act of 1964 ( 42 U.S.C. 2000a et seq. ), title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ), section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ), and section 1557 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18116 ).\n#### 10. Limitation\nNo Federal funds provided under this Act may be used for sex education or sexual health services that\u2014\n**(1)**\nwithhold health-promoting or life-saving information about sexuality-related topics, including HIV;\n**(2)**\nare medically inaccurate or incomplete;\n**(3)**\npromote gender or racial stereotypes or are unresponsive to gender or racial inequities;\n**(4)**\nfail to address the needs of sexually active young people;\n**(5)**\nfail to address the needs of pregnant or parenting young people;\n**(6)**\nfail to address the needs of survivors of interpersonal violence;\n**(7)**\nfail to address the needs of young people of all physical, developmental, or mental abilities;\n**(8)**\nfail to be inclusive of individuals with varying gender identities, gender expressions, and sexual orientations; or\n**(9)**\nare inconsistent with the ethical imperatives of medicine and public health.\n#### 11. Amendments to other laws\n##### (a) Amendment to the Public Health Service Act\nSection 2500 of the Public Health Service Act ( 42 U.S.C. 300ee ) is amended by striking subsections (b) through (d) and inserting the following:\n(b) Contents of programs All programs of education and information receiving funds under this title shall include information about the potential effects of intravenous substance use. .\n##### (b) Amendments to the Elementary and Secondary Education Act of 1965\nSection 8526 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7906 ) is amended\u2014\n**(1)**\nby striking paragraphs (3), (5), and (6);\n**(2)**\nby redesignating paragraph (4) as paragraph (3);\n**(3)**\nin paragraph (3), as redesignated by paragraph (2), by inserting or after the semicolon; and\n**(4)**\nby redesignating paragraph (7) as paragraph (4).\n#### 12. Funding\n##### (a) Authorization\nFor the purpose of carrying out this Act, there is authorized to be appropriated $100,000,000 for each of fiscal years 2026 through 2031. Amounts appropriated under this subsection shall remain available until expended.\n##### (b) Reservations of funds\n**(1) In general**\nThe Secretary\u2014\n**(A)**\nshall reserve not more than 30 percent of the amount authorized under subsection (a) for the purposes of awarding grants for sex education at elementary and secondary schools and youth-serving organizations under section 4;\n**(B)**\nshall reserve not more than 10 percent of the amount authorized under subsection (a) for the purpose of awarding grants for sex education at institutions of higher education under section 5;\n**(C)**\nshall reserve not more than 15 percent of the amount authorized under subsection (a) for the purpose of awarding grants for educator training under section 6;\n**(D)**\nshall reserve not more than 30 percent of the amount authorized under subsection (a) for the purpose of awarding grants for sexual health services for underserved youth under section 7; and\n**(E)**\nshall reserve not less than 5 percent of the amount authorized under subsection (a) for the purpose of carrying out the reporting and impact evaluation required under section 8.\n**(2) Research, training, and technical assistance**\nThe Secretary shall reserve not less than 10 percent of the amount authorized under subsection (a) for expenditures by the Secretary to provide, directly or through a competitive grant process, research, training, and technical assistance, including dissemination of research and information regarding effective and promising practices, providing consultation and resources, and developing resources and materials to support the activities of recipients of grants. In carrying out such functions, the Secretary shall collaborate with a variety of entities that have expertise in sex education and sexual health services standards setting, design, development, delivery, research, monitoring, and evaluation.\n##### (c) Reprogramming of abstinence only until marriage program funding\nThe unobligated balance of funds made available to carry out section 510 of the Social Security Act ( 42 U.S.C. 710 ) (as in effect on the day before the date of enactment of this Act) are hereby transferred and shall be used by the Secretary to carry out this Act. The amounts transferred and made available to carry out this Act shall remain available until expended.\n##### (d) Repeal of abstinence only until marriage program\nSection 510 of the Social Security Act ( 42 U.S.C. 710 ) is repealed.",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1910",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Real Education and Access for Healthy Youth Act of 2025",
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
        "updateDate": "2025-05-29T15:44:38Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3527ih.xml"
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
      "title": "Real Education and Access for Healthy Youth Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Real Education and Access for Healthy Youth Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the overall health and well-being of young people, including the promotion and attainment of lifelong sexual health and healthy relationships, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:33:52Z"
    }
  ]
}
```
